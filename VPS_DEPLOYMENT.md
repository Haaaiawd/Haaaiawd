# VPS 自托管部署方案

## 📋 方案概述

在 VPS 上自托管 pixel-profile 和 github-readme-terminal，避免公共 API 限速问题。

## 🚀 部署步骤

### 1. 准备工作

#### 1.1 创建 GitHub Personal Access Token
1. 访问 https://github.com/settings/tokens/new
2. 创建新 token，勾选 "repo" 和 "user" 权限
3. 复制 token，保存到安全位置

#### 1.2 准备 VPS 环境
```bash
# 更新系统
sudo apt update && sudo apt upgrade -y

# 安装 Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# 安装 Python 和 FFmpeg
sudo apt install python3 python3-pip ffmpeg -y
```

### 2. 部署 Pixel-Profile

#### 方式 A: Docker 部署（推荐）

```bash
# 克隆仓库
git clone https://github.com/LuciNyan/pixel-profile.git
cd pixel-profile

# 构建镜像
docker build -t pixel-profile .

# 运行容器
docker run -d \
  --name pixel-profile \
  -p 3000:3000 \
  -e PAT_1=你的_GITHUB_TOKEN \
  -e PORT=3000 \
  --restart always \
  pixel-profile
```

访问: `http://你的VPS_IP:3000`

#### 方式 B: Node.js 部署

```bash
# 安装 pnpm
npm install -g pnpm

# 克隆仓库
git clone https://github.com/LuciNyan/pixel-profile.git
cd pixel-profile

# 创建 .env 文件
echo "PAT_1=你的_GITHUB_TOKEN" > .env

# 安装依赖
pnpm install

# 启动服务
pnpm start
```

#### 使用 PM2 守护进程
```bash
# 安装 PM2
npm install -g pm2

# 启动服务
pm2 start pnpm --name "pixel-profile" -- start

# 设置开机自启
pm2 startup
pm2 save
```

### 3. 部署 GitHub-Readme-Terminal

```bash
# 安装依赖
pip3 install github-readme-terminal

# 创建生成脚本
cat > generate_terminal.py << 'EOF'
#!/usr/bin/env python3
import gifos

USERNAME = "Haaaiawd"

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
EOF

# 设置环境变量
export GITHUB_TOKEN=你的_GITHUB_TOKEN

# 运行脚本
python3 generate_terminal.py

# 生成的 GIF 在 output.gif
```

### 4. 配置 Nginx 反向代理（可选）

```bash
# 安装 Nginx
sudo apt install nginx -y

# 创建配置文件
sudo nano /etc/nginx/sites-available/pixel-profile
```

配置内容：
```nginx
server {
    listen 80;
    server_name your-domain.com;

    # Pixel-Profile
    location /pixel-profile/ {
        proxy_pass http://localhost:3000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # 静态文件（GIF）
    location /images/ {
        alias /path/to/images/;
        autoindex off;
    }
}
```

启用配置：
```bash
sudo ln -s /etc/nginx/sites-available/pixel-profile /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 5. 设置定时任务

```bash
# 编辑 crontab
crontab -e
```

添加：
```cron
# 每天凌晨 2 点更新 terminal GIF
0 2 * * * cd /path/to/github-readme-terminal && /usr/bin/python3 generate_terminal.py && mv output.gif /path/to/images/terminal.gif
```

### 6. 更新 README.md

将 README.md 中的链接替换为自托管地址：

```markdown
<!-- Pixel Profile -->
<picture decoding="async" loading="lazy">
  <source media="(prefers-color-scheme: light)" srcset="http://你的VPS_IP:3000/api/github-stats?username=Haaaiawd&theme=crt">
  <source media="(prefers-color-scheme: dark)" srcset="http://你的VPS_IP:3000/api/github-stats?username=Haaaiawd&theme=crt">
  <img alt="github stats" src="http://你的VPS_IP:3000/api/github-stats?username=Haaaiawd&theme=crt">
</picture>

<!-- Terminal GIF -->
<img src="http://你的VPS_IP/images/terminal.gif" alt="Terminal GIF" />
```

## 🔧 配置 SSL（推荐）

使用 Let's Encrypt 免费 SSL 证书：

```bash
# 安装 Certbot
sudo apt install certbot python3-certbot-nginx -y

# 获取证书
sudo certbot --nginx -d your-domain.com

# 自动续期
sudo certbot renew --dry-run
```

更新 README 使用 HTTPS：
```markdown
http://your-domain.com → https://your-domain.com
```

## 📊 监控和维护

### 查看日志
```bash
# Docker 日志
docker logs pixel-profile

# PM2 日志
pm2 logs pixel-profile

# Nginx 日志
sudo tail -f /var/log/nginx/error.log
```

### 重启服务
```bash
# Docker
docker restart pixel-profile

# PM2
pm2 restart pixel-profile

# Nginx
sudo systemctl restart nginx
```

## ⚠️ 注意事项

1. **GitHub API 限速**：即使自托管，GitHub API 仍有 5000 次/小时的限制
2. **防火墙**：确保 VPS 防火墙开放 80、443、3000 端口
3. **安全性**：不要在代码中硬编码 GitHub Token，使用环境变量
4. **备份**：定期备份配置和生成的文件

## 🎯 快速测试

部署完成后，在浏览器访问：
- Pixel-Profile: `http://你的VPS_IP:3000/api/github-stats?username=Haaaiawd&theme=crt`
- Terminal GIF: `http://你的VPS_IP/images/terminal.gif`

如果都能正常访问，就可以更新 README.md 了。
