#!/bin/zsh

# Navigate to your repo
cd . || exit

# Create dummy files and commit them
for i in {1..15}
do
  echo "Dummy file number $i" > "file$i.txt"   # Create a new file
  git add "file$i.txt"                         # Stage the file for commit
  git commit -m "Automated commit $i"          # Commit the changes
done

# Push changes to GitHub
git push origin main

