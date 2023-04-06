def main():
    print('mailbox read test')
    mbox = mailbox.mbox(sys.argv[1])
    for msg in mbox:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(msg)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
if __name__ == "__main__":
    main()