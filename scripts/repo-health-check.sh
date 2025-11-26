#!/bin/bash
echo "Repository Health Check"
echo "=========================="

# Текущая ветка
echo "Current branch: $(git branch --show-current)"

# Размер репозитория
echo "Repository size:"
git count-objects -vH

# Последние коммиты
echo "Recent activity (last 5 commits):"
git log --oneline -5 --format="  %C(green)%h%C(reset) %s"

# Проверка подмодулей
if [ -f .gitmodules ]; then
    echo "Submodules status:"
    git submodule status
else
    echo "No submodules configured"
fi

# Проверка больших файлов
echo "Large files in history (top 5):"
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  awk '/^blob/ {if($3 > 100000) print $4, $3/1024 " KB"}' | \
  sort -k2 -nr | head -5

# Проверка .gitignore эффективности
echo "Checking for potentially ignored files:"
find . -name "*.pyc" -o -name "__pycache__" -o -name ".coverage" 2>/dev/null | head -5

echo "Health check complete!"
echo "Tips: Run 'git gc --aggressive' to optimize repository"
