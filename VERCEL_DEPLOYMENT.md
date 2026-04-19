# Vercel 部署方案（推荐）

## 📋 方案对比

### Vercel vs VPS

| 特性 | Vercel | VPS |
|------|--------|-----|
| **部署难度** | ⭐ 极简单（一键部署） | ⭐⭐⭐ 需要配置 |
| **维护成本** | ⭐ 无需维护 | ⭐⭐⭐ 需要自己维护 |
| **HTTPS** | ✅ 自动配置 | ⚠️ 需要手动配置 |
| **CDN** | ✅ 全球 CDN | ⚠️ 需要额外配置 |
| **成本** | ✅ 免费额度充足 | ⚠️ 需要支付服务器费用 |
| **自定义域名** | ✅ 支持 | ✅ 支持 |
| **控制权** | ⚠️ 受限 | ✅ 完全控制 |
| **适合场景** | 前端项目、API 服务 | 复杂后端、多服务 |

**推荐：Vercel** - 对于 pixel-profile 这种项目，Vercel 更简单、更快、免费

---

## 🚀 Vercel 部署步骤

### 1. 准备工作

#### 1.1 创建 GitHub Personal Access Token
1. 访问 https://github.com/settings/tokens/new
2. 创建新 token，勾选 "repo" 和 "user" 权限
3. 复制 token

#### 1.2 注册 Vercel
1. 访问 https://vercel.com/signup
2. 使用 GitHub 账号登录
3. 授权 Vercel 访问你的 GitHub 仓库

### 2. 部署 Pixel-Profile

#### 方式 A: 使用 Vercel 一键部署（推荐）

1. 访问 pixel-profile 官方部署链接：
   https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FLuciNyan%2Fpixel-profile

2. 配置环境变量：
   - `PAT_1`: 你的 GitHub Token
   - `PORT`: `3000`

3. 点击 "Deploy"

4. 等待部署完成（约 2-3 分钟）

5. 获取部署地址，格式如：`https://pixel-profile-xxx.vercel.app`

#### 方式 B: Fork 仓库后部署

1. Fork pixel-profile 仓库到你的账号

2. 在 Vercel 中：
   - 点击 "Add New" > "Project"
   - 选择你 fork 的仓库
   - 配置环境变量 `PAT_1`
   - 点击 "Deploy"

### 3. 配置自定义域名

#### 3.1 在 Vercel 中添加域名

1. 进入项目 Settings > Domains
2. 点击 "Add Domain"
3. 输入你的域名（如 `pixel.yourdomain.com`）
4. Vercel 会显示 DNS 配置信息

#### 3.2 配置 DNS 记录

在你的域名 DNS 管理面板添加：

```
类型: CNAME
名称: pixel
值: cname.vercel-dns.com
```

或使用 A 记录（如果 Vercel 提供）：

```
类型: A
名称: pixel
值: 76.76.21.21
```

#### 3.3 等待 DNS 生效

通常需要 5-10 分钟，最多 24 小时

### 4. 部署 GitHub-Readme-Terminal

由于 github-readme-terminal 需要运行 Python 脚本生成 GIF，有几种方案：

#### 方案 A: 本地生成后上传到 Vercel（推荐）

1. 在本地安装依赖：
```bash
pip install github-readme-terminal
```

2. 创建生成脚本：
```python
import gifos
import os

USERNAME = "Haaaiawd"
GITHUB_TOKEN = "你的_GITHUB_TOKEN"

os.environ['GITHUB_TOKEN'] = GITHUB_TOKEN

t = gifos.Terminal(width=320, height=240, xpad=5, ypad=5)
t.gen_text(text=f"╭─ {USERNAME}@github ─╮", row_num=1, contin=True)
t.gen_text(text="│", row_num=2, contin=True)

try:
    github_stats = gifos.utils.fetch_github_stats(user_name=USERNAME)
    t.gen_text(text=f"│ 📦 Repos: {github_stats.total_public_repos}", row_num=3, contin=True)
    t.gen_text(text=f"│ ⭐ Stars: {github_stats.total_stars}", row_num=4, contin=True)
    t.gen_text(text=f"│ 🔄 Followers: {github_stats.followers}", row_num=5, contin=True)
    t.gen_text(text=f"│ 📝 Following: {github_stats.following}", row_num=6, contin=True)
except Exception as e:
    print(f"Error: {e}")
    t.gen_text(text="│ 📦 Repos: Loading...", row_num=3, contin=True)
    t.gen_text(text="│ ⭐ Stars: Loading...", row_num=4, contin=True)
    t.gen_text(text="│ 🔄 Followers: Loading...", row_num=5, contin=True)
    t.gen_text(text="│ 📝 Following: Loading...", row_num=6, contin=True)

t.gen_text(text="│", row_num=7, contin=True)
t.gen_text(text=f"╰─────────────────────╯", row_num=8, contin=True)
t.gen_gif()
```

3. 运行脚本生成 GIF：
```bash
python generate_terminal.py
```

4. 将生成的 `output.gif` 上传到：
   - 你的 Vercel 项目（通过 Git）
   - 或图床服务（如 ImgBB）

#### 方式 B: 使用 GitHub Actions 生成

保持现有的 GitHub Actions 配置，让 Actions 自动生成 GIF 并推送到 `output` 分支。

### 5. 更新 README.md

使用 Vercel 部署地址：

```markdown
<!-- Pixel Profile -->
<picture decoding="async" loading="lazy">
  <source media="(prefers-color-scheme: light)" srcset="https://your-vercel-app.vercel.app/api/github-stats?username=Haaaiawd&theme=crt">
  <source media="(prefers-color-scheme: dark)" srcset="https://your-vercel-app.vercel.app/api/github-stats?username=Haaaiawd&theme=crt">
  <img alt="github stats" src="https://your-vercel-app.vercel.app/api/github-stats?username=Haaaiawd&theme=crt">
</picture>

<!-- Terminal GIF -->
<img src="https://raw.githubusercontent.com/Haaaiawd/Haaaiawd/output/terminal.gif" alt="Terminal GIF" />
```

或使用自定义域名：

```markdown
<!-- Pixel Profile -->
<picture decoding="async" loading="lazy">
  <source media="(prefers-color-scheme: light)" srcset="https://pixel.yourdomain.com/api/github-stats?username=Haaaiawd&theme=crt">
  <source media="(prefers-color-scheme: dark)" srcset="https://pixel.yourdomain.com/api/github-stats?username=Haaaiawd&theme=crt">
  <img alt="github stats" src="https://pixel.yourdomain.com/api/github-stats?username=Haaaiawd&theme=crt">
</picture>
```

### 6. 设置自动更新（可选）

#### 方式 A: Vercel 自动部署

Vercel 默认会在每次 Git push 时自动重新部署，无需额外配置。

#### 方式 B: 定时更新 Terminal GIF

使用 GitHub Actions 定时生成 GIF（已配置），或使用 cron-job.org 等服务定时调用你的生成脚本。

### 7. 监控和维护

#### 查看部署日志
1. 进入 Vercel 项目
2. 点击 "Deployments"
3. 查看最新的部署日志

#### 环境变量管理
1. 进入 Settings > Environment Variables
2. 可以随时更新 PAT_1 等变量
3. 更新后需要重新部署

#### 查看使用量
1. 进入 Settings > Usage
2. 查看带宽、函数调用等使用情况
3. Vercel 免费额度：100GB 带宽/月

## 🎯 快速测试

部署完成后，在浏览器访问：
- Pixel-Profile: `https://your-vercel-app.vercel.app/api/github-stats?username=Haaaiawd&theme=crt`
- 或自定义域名: `https://pixel.yourdomain.com/api/github-stats?username=Haaaiawd&theme=crt`

## ⚠️ 注意事项

1. **GitHub API 限速**：5000 次/小时，即使自托管也有限制
2. **免费额度**：Vercel 免费额度通常足够个人使用
3. **环境变量**：不要在代码中硬编码 Token，使用环境变量
4. **域名 DNS**：配置后需要等待生效时间

## 📊 成本对比

### Vercel 免费版
- ✅ 100GB 带宽/月
- ✅ 无限项目
- ✅ 自动 HTTPS
- ✅ 全球 CDN
- ✅ 自定义域名
- 💰 $0/月

### VPS（以阿里云轻量应用服务器为例）
- 💰 ¥24/月（1核2G）
- 💰 ¥36/月（2核4G）
- 需要额外配置域名和 HTTPS

**结论：Vercel 免费版完全够用，且更简单**

## 🎉 完成

现在你的 GitHub Profile 使用了：
- ✅ 自托管的 pixel-profile（Vercel）
- ✅ 自动 HTTPS
- ✅ 全球 CDN 加速
- ✅ 自定义域名支持
- ✅ 零成本部署
