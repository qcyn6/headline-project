from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, func, update
from ..cache.news_cache import get_cached_categories, set_cache_categories, get_cached_news_list, set_cache_news_list, \
    cache_news_detail, get_cached_news_detail,get_cached_related_news,cache_related_news
from ..models.news import Category,News
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas.base import NewsItemBase

async def get_categories(db: AsyncSession,skip: int = 0,limit: int = 100):
    # 先尝试从缓存中获取数据
    cached_categories = await get_cached_categories()
    if cached_categories:
        return cached_categories

    stmt = select(Category).offset(skip).limit(limit)
    result = await db.execute(stmt)
    categories = result.scalars().all()     # ORM对象

    # 写入缓存
    if categories:
        categories = jsonable_encoder(categories)    # 将ORM对象转换成普通的 Python 字典 / 列表
        await set_cache_categories(categories)
    # 返回数据
    return categories

async def get_news_list(db: AsyncSession,category_id: int,skip: int = 0,limit: int = 10):
    # 先尝试从缓存中获取新闻列表
    page = skip // limit + 1
    cached_list = await get_cached_news_list(category_id,page,limit)    # 缓存数据 json
    if cached_list:
        # return cached_list
        return [News(**item) for item in cached_list]   # 转成ORM对象

    # 查询指定分类下的所有新闻
    stmt = select(News).where(News.category_id == category_id).offset(skip).limit(limit)
    result = await db.execute(stmt)
    news_list = result.scalars().all()

    # 写入缓存
    if news_list:
        # 先把ORM数据转换成字典才能写入缓存
        # ORM 转成 Pydantic 再转为 字典
        # by_alias=False 忽略别名,保存Python风格,因为redis数据是给后端用的
        news_data = [NewsItemBase.model_validate(item).model_dump(mode='json',by_alias=False) for item in news_list]
        await set_cache_news_list(category_id,page,limit,news_data)
    # 返回数据
    return news_list


async def get_news_count(db: AsyncSession,category_id: int):
    # 查询指定分类下的新闻总数
    stmt = select(func.count(News.id)).where(News.category_id == category_id)
    result = await db.execute(stmt)
    return result.scalar_one()  # 只能有一个结果,否则报错

async def get_news_detail(db: AsyncSession,news_id: int):
    # 先尝试从缓存获取新闻详情
    cached_detail = await get_cached_news_detail(news_id)
    if cached_detail:
        return News(**cached_detail)

    stmt = select(News).where(News.id == news_id)
    result = await db.execute(stmt)
    news = result.scalar_one_or_none()
    # 写入缓存
    if news:
        news_data = jsonable_encoder(news)
        await cache_news_detail(news_id, news_data)

    return news

async def increase_news_views(db: AsyncSession, news_id: int):
    stmt = update(News).where(News.id == news_id).values(views=News.views + 1)
    result = await db.execute(stmt)
    await db.commit()
    # 更新 -> 检查数据库是否真的命中了数据 -> 命中了返回True
    return result.rowcount > 0

async def get_related_news(db: AsyncSession,news_id: int,category_id: int,limit: int = 5):
    # 先尝试从缓存获取相关新闻
    cached_related = await get_cached_related_news(news_id, category_id)
    if cached_related:
        return cached_related

    stmt = select(News).where(
        News.category_id == category_id,News.id != news_id
    ).order_by(
        News.views.desc(),
        News.publish_time.desc()
    ).limit(limit)
    result = await db.execute(stmt)
    # return result.scalars().all()
    related_news = result.scalars().all()
    related_list = [{
        "id": news_detail.id,
        "title": news_detail.title,
        "content": news_detail.content,
        "image": news_detail.image,
        "author": news_detail.author,
        "publishTime": news_detail.publish_time.strftime("%Y-%m-%d %H:%M:%S"),
        "categoryId": news_detail.category_id,
        "views": news_detail.views,
    } for news_detail in related_news]

    # 写入缓存
    if related_list:
        await cache_related_news(news_id, category_id, related_list)

    return related_list