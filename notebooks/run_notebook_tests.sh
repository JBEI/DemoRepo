#!/bin/zsh

for f in *.ipynb
do
  echo "Testing $f ..."
  jupyter nbconvert --to notebook --execute "$f"
done
