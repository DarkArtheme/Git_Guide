from db_manager import DBManager
from io_manager import IOManager


# this is main
def main():
    db = DBManager()
    IOManager.exec_cmd(["ls", "-l", "."])


if __name__ == "__main__":
    main()

# random comment
# another line
