@echo off
title The Magic Walnut Plant Shoppe - 1-Click Live Publisher
cd /d "H:\The Magic Walnut Plants Sales\website"

echo ============================================================================
echo   THE MAGIC WALNUT PLANT SHOPPE • 1-CLICK GITHUB PAGES PUBLISHER
echo   Domain: themagicwalnutplantshoppe.com
echo ============================================================================
echo.

if not exist ".git" (
    echo [1/4] Initializing local Git repository...
    git init
    git branch -M main
)

echo [2/4] Staging latest plant photos, catalog.json, and carnival games...
git add -A

set "STAMP=%DATE% %TIME%"
git commit -m "Sanctuary Weekly Drop & Site Update (%STAMP%)"

echo [3/4] Pushing to GitHub (iamdustins/the-magic-walnut-sanctuary)...
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    git remote add origin https://github.com/iamdustins/the-magic-walnut-sanctuary.git
)
git push -u origin main --force

echo.
echo ============================================================================
echo   SUCCESS! Your latest plant drop & site changes are pushed to GitHub!
echo   Live URL: https://themagicwalnutplantshoppe.com
echo   GitHub Pages Preview: https://iamdustins.github.io/the-magic-walnut-sanctuary/
echo ============================================================================
pause
