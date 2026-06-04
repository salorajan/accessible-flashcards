# PowerShell Script to Deploy to GitHub
# Make sure you are logged in to gh (run 'gh auth login' if not)

Write-Host "Step 1: Initializing Git..." -ForegroundColor Cyan
git init

Write-Host "Step 2: Adding files..." -ForegroundColor Cyan
# We include the dist/app.exe so it's downloadable from the GitHub Page
git add .

Write-Host "Step 3: Committing changes..." -ForegroundColor Cyan
git commit -m "Initial commit: Accessible Flashcards for the Blind"

Write-Host "Step 4: Creating GitHub Repository 'salorajan'..." -ForegroundColor Cyan
# This creates the repo on GitHub and pushes the current folder
gh repo create salorajan --public --source=. --remote=origin --push

Write-Host "Step 5: Enabling GitHub Pages..." -ForegroundColor Cyan
# This sets the 'main' branch as the source for GitHub Pages
gh repo edit salorajan --enable-pages --pages-branch main

Write-Host "`nSuccessfully Deployed!" -ForegroundColor Green
Write-Host "Your website will be live soon at: https://salorajan.github.io/salorajan/"
Write-Host "If your username is also 'salorajan', it might be at: https://salorajan.github.io/"
