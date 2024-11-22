

WORK_DIR=$(pwd)
SCRIPT_DIR=$(dirname "$0")
echo "$SCRIPT_DIR"
MANAGE_PY_DIR="$WORK_DIR/$SCRIPT_DIR/manage.py"
python "$MANAGE_PY_DIR" runserver
