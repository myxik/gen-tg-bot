INSERT = """INSERT INTO data (id, user_id, chat_id, prompt, natural_prompt, path_to_img, current_status) 
VALUES (%s, %s, %s, %s, %s, %s, %s);"""

FIND = """SELECT * FROM data 
WHERE user_id = %s AND current_status = 0;
"""

UPDATE = """UPDATE data 
SET natural_prompt = %s, current_status = %s 
WHERE id = %s;"""


HELLO_STR = """
Hi! This is simple bot for image generation (and dataset collection). You can generate for free in any amounts (safety checker also disabled). For now, it runs only on my 25 usd that i spent on hardware.

Intended use: firstly use /add_prompt command and then /add_natural_prompt consequently. Please take tags from danbooru. Can be found here https://danbooru.donmai.us/tags
natural prompts should be natural, you can be as natural as you want to

Example:
/add_prompt 1boy, realistic, cyberpunk *hit send message*
/add_natural_prompt one boy in realistic manner drawn in cyberpunk like style

If you can and wish to please donate to donation alerts, all money with prefix [BOT HARDWARE] go to make this bot absolutely free (on hardware, no profit taken unless you specify). Once we ran out of cash I will shut it down.

https://www.donationalerts.com/r/yamazakij
"""