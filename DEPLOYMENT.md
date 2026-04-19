# GitHub Profile 部署指南

## 📋 前置步骤

### 1. 创建 GitHub 仓库
1. 访问 https://github.com/new
2. 仓库名称：`Haaaiawd`
3. 设为 Public
4. 不要勾选 "Add a README file"

### 2. 上传文件
将以下文件上传到你的 GitHub 仓库：
- `README.md`
- `.github/workflows/pixel-profile.yml`
- `.github/workflows/terminal.yml`
- `generate_terminal.py`
- `requirements.txt`

## 🚀 启用 GitHub Actions

### 1. 启用 Actions
1. 进入你的仓库
2. 点击 "Settings" 标签
3. 左侧菜单选择 "Actions" > "General"
4. 在 "Actions permissions" 中选择 "Allow all actions and reusable workflows"
5. 点击 "Save"

### 2. 手动触发 Actions
1. 点击 "Actions" 标签
2. 在左侧选择 "generate-and-upload-card" workflow
3. 点击 "Run workflow" > "Run workflow" 按钮
4. 等待 workflow 完成（约 1-2 分钟）
5. 同样操作触发 "generate-terminal-gif" workflow

### 3. 创建 output 分支
Actions 会自动创建 `output` 分支并上传生成的图片。你可以在仓库的分支切换页面看到这个分支。

## 🎨 自定义配置

### Pixel Profile 主题
编辑 `.github/workflows/pixel-profile.yml` 中的主题参数：

```yaml
outputs: |
  dist/github-stats?username=Haaaiawd&screen_effect=false&theme=fuji&dithering=true&hide=avatar
  dist/github-stats-dark?username=Haaaiawd&theme=fuji&hide=avatar&avatar_border=false&screen_effect=true
```

可用主题：
- `fuji` - 富士山主题（推荐）
- `rainbow` - 彩虹主题
- `summer` - 夏日主题
- `journey` - 旅程主题
- `road_trip` - 公路旅行主题
- `monica` - Monica 主题
- `lax` - LAX 主题
- `crt` - CRT 复古显示器主题

### Terminal 配置
编辑 `generate_terminal.py` 来自定义终端显示内容。

## 📝 更新 README

如果生成的图片路径不对，编辑 `README.md` 中的图片链接：

```markdown
<!-- Pixel Profile -->
<picture decoding="async" loading="lazy">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Haaaiawd/Haaaiawd/output/github-stats.svg">
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Haaaiawd/Haaaiawd/output/github-stats-dark.svg">
  <img alt="github stats" src="https://raw.githubusercontent.com/Haaaiawd/Haaaiawd/output/github-stats.svg">
</picture>

<!-- Terminal GIF -->
<img src="https://raw.githubusercontent.com/Haaaiawd/Haaaiawd/output/terminal.gif" alt="Terminal GIF" />
```

## ⚠️ 故障排除

### Pixel Profile 不显示
- 检查 Actions workflow 是否成功运行
- 确认 output 分支是否创建
- 检查 README.md 中的图片路径是否正确

### Terminal GIF 不生成
- Terminal GIF 生成可能需要更长时间（5-10 分钟）
- 检查 Actions 日志查看错误信息
- 可能需要添加 GitHub Token 到 Secrets

### 添加 GitHub Token（可选）
1. 访问 https://github.com/settings/tokens/new
2. 创建新 token，勾选 "repo" 权限
3. 复制 token
4. 进入仓库 Settings > Secrets and variables > Actions
5. 点击 "New repository secret"
6. Name: `GITHUB_TOKEN`
7. Secret: 粘贴你的 token
8. 点击 "Add secret"

## 🎉 完成

现在你的 GitHub Profile 应该已经美化了！访问 https://github.com/Haaaiawd 查看效果。
