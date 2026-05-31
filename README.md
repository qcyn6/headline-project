# 📰 Headline News App

基于 **FastAPI + Vue 3** 的全栈新闻应用，提供新闻浏览、用户认证、收藏管理、浏览历史等功能，集成 **Redis 缓存优化** 提升性能。

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)
![Vue](https://img.shields.io/badge/Vue-3.x-brightgreen?logo=vue.js)
![MySQL](https://img.shields.io/badge/MySQL-8.0-blue?logo=mysql)
![Redis](https://img.shields.io/badge/Redis-7.x-red?logo=redis)
![License](https://img.shields.io/badge/License-MIT-yellow)

</div>

## ✨ 功能特性

- ✅ **用户系统**：注册、登录、JWT 认证、个人信息管理、密码修改
- ✅ **新闻浏览**：分类浏览、分页列表、详情查看、相关推荐
- ✅ **收藏功能**：添加/取消收藏、收藏列表、收藏状态检查
- ✅ **浏览历史**：自动记录、历史列表、单条删除、清空历史
- ✅ **Redis 缓存**：分类缓存、列表缓存、防缓存穿透设计
- ✅ **国际化**：支持中文/英文切换（i18n）
- ✅ **响应式设计**：移动端友好，适配多种设备
- ✅ **统一响应**：标准化的 API 响应格式和异常处理

## 🛠️ 技术栈

### 后端技术

| 技术 | 版本 | 说明 |
|------|------|------|
| Python | 3.12+ | 编程语言 |
| FastAPI | 0.100+ | 异步 Web 框架 |
| SQLAlchemy | 2.0 | 异步 ORM |
| MySQL | 8.0 | 关系型数据库 |
| Redis | 7.x | 缓存中间件 |
| Pydantic | v2 | 数据验证与序列化 |
| Passlib + bcrypt | - | 密码加密 |
| Uvicorn | - | ASGI 服务器 |

### 前端技术

| 技术 | 版本 | 说明 |
|------|------|------|
| Vue | 3.x | 渐进式 JavaScript 框架 |
| Vite | 7.x | 前端构建工具 |
| Pinia | 3.x | Vue 状态管理 |
| Vue Router | 4.x | 路由管理 |
| Axios | 1.x | HTTP 请求库 |
| Vant | 4.x | 移动端 UI 组件库 |
| Vue I18n | 9.x | 国际化支持 |
| Marked | 16.x | Markdown 解析 |
| DOMPurify | 3.x | XSS 防护 |

## 📁 项目结构

```
headline-project/
── backend/                    # 后端服务
│   ├── main.py                 # 应用入口
│   ├── config/                 # 配置层
│   │   ├── db_conf.py          # 数据库配置
│   │   └── cache_conf.py       # Redis 配置
│   ├── models/                 # ORM 模型
│   │   ├── news.py             # 新闻和分类模型
│   │   ├── users.py            # 用户和令牌模型
│   │   ├── favorite.py         # 收藏模型
│   │   └── history.py          # 历史模型
│   ├── schemas/                # Pydantic 模型
│   │   ├── base.py             # 基础模型
│   │   ├── users.py            # 用户相关
│   │   ├── favorite.py         # 收藏相关
│   │   └── history.py          # 历史相关
│   ├── routers/                # 路由层
│   │   ├── news.py             # 新闻接口
│   │   ├── users.py            # 用户接口
│   │   ├── favorite.py         # 收藏接口
│   │   └── history.py          # 历史接口
│   ├── crud/                   # 数据操作层
│   │   ├── news.py             # 新闻 CRUD
│   │   ├── news_cache.py       # 新闻缓存逻辑
│   │   ├── users.py            # 用户 CRUD
│   │   ├── favorite.py         # 收藏 CRUD
│   │   └── history.py          # 历史 CRUD
│   ├── cache/                  # 缓存层
│   │   └── news_cache.py       # 缓存策略
│   ├── utils/                  # 工具模块
│   │   ├── auth.py             # JWT 认证
│   │   ├── security.py         # 密码加密
│   │   ├── response.py         # 响应封装
│   │   └── exception.py        # 异常处理
│   └── db/
│       └── database.sql        # 数据库脚本
│
└── frontend/                   # 前端应用
    ├── src/
    │   ├── views/              # 页面组件
    │   │   ├── Home.vue        # 首页
    │   │   ├── NewsDetail.vue  # 新闻详情
    │   │   ├── Category.vue    # 分类页
    │   │   ├── Favorite.vue    # 收藏页
    │   │   ├── History.vue     # 历史页
    │   │   ├── Login.vue       # 登录页
    │   │   ├── Register.vue    # 注册页
    │   │   ├── Profile.vue     # 个人中心
    │   │   └── Settings.vue    # 设置页
    │   ├── components/         # 公共组件
    │   │   ├── NewsItem.vue    # 新闻项
    │   │   └── TabBar.vue      # 底部导航
    │   ├── store/              # Pinia 状态管理
    │   │   ├── user.js         # 用户状态
    │   │   ├── news.js         # 新闻状态
    │   │   ├── favorite.js     # 收藏状态
    │   │   ├── history.js      # 历史状态
    │   │   ├── theme.js        # 主题状态
    │   │   └── language.js     # 语言状态
    │   ├── router/             # 路由配置
    │   ├── i18n/               # 国际化
    │   │   └── locales/        # 语言包
    │   └── config/             # 配置
    │       └── api.js          # API 配置
    ├── package.json
    └── vite.config.js
```

## 🚀 快速开始

### 环境要求

- Python 3.12+
- Node.js 16+
- MySQL 8.0+
- Redis 7.x+

### 1️⃣ 后端启动

```bash
# 进入后端目录
cd backend

# 创建并激活虚拟环境
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 安装依赖
pip install fastapi uvicorn[standard] sqlalchemy aiomysql redis pydantic passlib[bcrypt] python-jose[cryptography]

# 创建数据库
mysql -u root -p
> CREATE DATABASE news_app DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
> exit

# 导入数据库结构和测试数据
mysql -u root -p news_app < db/database.sql

# 修改配置（根据需要）
# 编辑 config/db_conf.py 修改数据库密码
# 编辑 config/cache_conf.py 修改 Redis 配置

# 启动服务
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

后端启动后访问：
- API 文档：http://localhost:8000/docs
- 备用文档：http://localhost:8000/redoc

### 2️⃣ 前端启动

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

前端启动后访问：http://localhost:5173

### 3️ 生产构建

```bash
# 前端构建
cd frontend
npm run build

# 构建产物在 frontend/dist 目录
# 可使用 Nginx 或其他 Web 服务器部署
```

## 📡 API 接口文档

### 新闻模块 `/api/news`

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|:----:|
| GET | `/api/news/categories` | 获取新闻分类 | 否 |
| GET | `/api/news/list` | 获取新闻列表（分页） | 否 |
| GET | `/api/news/detail` | 获取新闻详情 | 否 |

**查询参数：**
- `list`: `categoryId`, `page`, `pageSize`
- `detail`: `id`

### 用户模块 `/api/user`

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|:----:|
| POST | `/api/user/register` | 用户注册 | 否 |
| POST | `/api/user/login` | 用户登录 | 否 |
| GET | `/api/user/info` | 获取用户信息 | ✅ |
| PUT | `/api/user/update` | 修改用户信息 | ✅ |
| PUT | `/api/user/password` | 修改密码 | ✅ |

### 收藏模块 `/api/favorite`

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|:----:|
| GET | `/api/favorite/check` | 检查收藏状态 | ✅ |
| POST | `/api/favorite/add` | 添加收藏 | ✅ |
| DELETE | `/api/favorite/remove` | 取消收藏 | ✅ |
| GET | `/api/favorite/list` | 获取收藏列表 | ✅ |
| DELETE | `/api/favorite/clear` | 清空收藏 | ✅ |

### 历史模块 `/api/history`

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|:----:|
| POST | `/api/history/add` | 添加浏览历史 | ✅ |
| GET | `/api/history/list` | 获取历史列表 | ✅ |
| DELETE | `/api/history/delete/{news_id}` | 删除单条历史 | ✅ |
| DELETE | `/api/history/clear` | 清空历史 | ✅ |

### 认证方式

需要认证的接口在请求头中携带 Token：

```http
Authorization: Bearer <your-token>
```

Token 有效期：**7 天**

### 统一响应格式

```json
{
  "code": 200,
  "message": "success",
  "data": {}
}
```

**分页响应：**
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "list": [],
    "total": 100,
    "hasMore": true
  }
}
```

## 💾 缓存策略

项目使用 Redis 实现多级缓存，减少数据库查询压力：

| 数据类型 | 缓存 Key | 过期时间 | 说明 |
|----------|---------|---------|------|
| 新闻分类 | `news:categories` | 2 小时 | 分类数据稳定，缓存时间长 |
| 新闻列表 | `news_list:{catId}:{page}:{size}` | 30 分钟 | 按分类和分页缓存 |
| 新闻详情 | `news:detail:{id}` | 5 分钟 | 详情更新频繁，缓存时间短 |
| 相关推荐 | `news:related:{newsId}:{catId}` | 30 分钟 | 推荐列表缓存 |

### 缓存穿透防护

- ✅ 空结果也缓存（防止恶意请求）
- ✅ 明确判断 `None` vs 空列表
- ✅ 异常捕获避免缓存服务中断

## 🗄️ 数据库设计

### 核心表结构

| 表名 | 说明 | 关键字段 |
|------|------|---------|
| `user` | 用户表 | id, username, password, avatar, gender |
| `user_token` | 令牌表 | id, user_id, token, expires_at |
| `news_category` | 分类表 | id, name, sort_order |
| `news` | 新闻表 | id, title, content, image, views, category_id |
| `favorite` | 收藏表 | id, user_id, news_id, created_at |
| `history` | 历史表 | id, user_id, news_id, viewed_at |

详细建表语句见 `backend/db/database.sql`

##  安全特性

- ✅ **密码加密**：使用 bcrypt 算法，防止明文存储
- ✅ **JWT 认证**：基于 Token 的无状态认证
- ✅ **SQL 注入防护**：SQLAlchemy ORM 参数化查询
- ✅ **XSS 防护**：前端使用 DOMPurify 净化内容
- ✅ **异常处理**：四层异常捕获，防止信息泄露
- ✅ **CORS 配置**：跨域请求控制

## 🌍 国际化

支持中英文切换，语言包位置：

```
frontend/src/i18n/locales/
├── zh-CN.js    # 中文
└── en-US.js    # 英文
```

## 🎨 UI 组件

使用 **Vant 4** 移动端组件库，提供：

- 底部导航栏
- 列表组件
- 表单组件
- 弹窗提示
- 加载状态

## 🐛 调试技巧

### 后端调试

```bash
# 开启调试模式
# 在 main.py 中设置 DEBUG_MODE = True
# 错误响应会包含详细堆栈信息
```

### 前端调试

```javascript
// 在浏览器控制台查看
console.log(process.env)

// 查看 API 请求
// Network 面板过滤 XHR 请求
```

### Redis 监控

```bash
# 监控所有 Redis 操作
redis-cli MONITOR

# 查看缓存键
redis-cli KEYS "news:*"

# 查看缓存值
redis-cli GET "news:categories"

# 查看缓存过期时间
redis-cli TTL "news:categories"
```

## 📊 性能优化

- ✅ **异步处理**：FastAPI + SQLAlchemy AsyncSession
- ✅ **Redis 缓存**：减少数据库查询
- ✅ **分页查询**：避免一次性加载大量数据
- ✅ **索引优化**：外键字段添加索引
- ✅ **连接池**：数据库连接复用

## 🚧 开发注意事项

1. **虚拟环境**：始终在虚拟环境中安装依赖
2. **数据库配置**：修改 `db_conf.py` 中的密码
3. **Redis 服务**：确保 Redis 服务已启动
4. **跨域问题**：前端 API 地址配置在 `api.js`
5. **缓存更新**：修改数据后注意清除相关缓存

##  开发规范

- 后端遵循 RESTful API 设计规范
- 使用 Pydantic 进行数据验证
- 统一异常处理和响应格式
- 前端使用 Composition API
- 组件化开发，状态管理使用 Pinia

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- [FastAPI](https://fastapi.tiangolo.com/)
- [Vue.js](https://vuejs.org/)
- [Vant](https://vant-ui.github.io/vant/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

---

<div align="center">

**Made with ❤️ by [qcyn6](https://github.com/qcyn6)**

如果这个项目对你有帮助，欢迎 ⭐ Star 支持！

</div>
