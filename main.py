from config import config


def main():
    try:
        a = config()

        server = a.server
        token_url = a.token_url
        tvu = a.token_validation_url
        sgu = a.student_group_url
        jid = a.client_id
        moo = a.moo
        js = a.juice_secret





    except Exception as ex:
        print ex

if __name__ == "__main__":
    main()