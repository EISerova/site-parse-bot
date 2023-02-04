from bad_words import BAD_WORDS
from config import GAPON_EMAILS, SITE_ADDRESS
from settings import TEXT_POSITION_IN_POST

gapon_comments_id = []
bad_comments_id = {}


def get_gapon_comments(post, gapon_comments_id):
    "Получение id комментариев по списку эл.почт юзеров."
    user_email = post[5]
    if user_email in GAPON_EMAILS:
        post_id = post[1]
        gapon_comments_id.append(post_id[4:])

    return gapon_comments_id


def get_bad_comments(post, bad_comments_id):
    "Получение id, текста и времени комментариев по списку запрещенных слов."

    text = post[TEXT_POSITION_IN_POST[len(post)]]

    for bad_word in BAD_WORDS:
        if bad_word in text:
            post_id = post[1]
            bad_comments_id[
                post[1]
            ] = f"ссылка - {SITE_ADDRESS}/{post_id[4:]}, текст - {text}, время {post[0]}"
    return bad_comments_id


def from_string_to_column(gapon_comments_id):
    "Представление данных из строки в виде столбца (удобнее вносить в эксель)."

    column = ""
    for id in gapon_comments_id:
        column += id
        column += "\n"
    return column
