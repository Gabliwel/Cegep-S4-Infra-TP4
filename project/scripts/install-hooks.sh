GIT_DIR=$(git rev-parse --git-dir)
echo "Running form: " $PWD
echo "Git dir is: " $GIT_DIR

echo "Installing hook...."
echo "Linking: " $GIT_DIR/hook/pre-commit
echo "To: " ./project/scripts/pre-commit.sh

ln -s ../../project/scripts/pre-commit.sh $GIT_DIR/hooks/pre-commit
echo "DONE"
