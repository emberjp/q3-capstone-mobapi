INSERT INTO
    games (name,url_name)
VALUES
    ('League of Legends','lol');    

INSERT INTO
    roles (name)
VALUES
    ('assassin'),
    ('fighter'),
    ('mage'),
    ('marksman'),
    ('support'),
    ('tank');

INSERT INTO
    champions (name,img_url,info,game_id)
VALUES
    ('Ahri','placeholder','placeholder',(SELECT id FROM games WHERE url_name='lol')),
    ('Sivir','placeholder','placeholder',(SELECT id FROM games WHERE url_name='lol')),
    ('Elise','placeholder','placeholder',(SELECT id FROM games WHERE url_name='lol')),
    ('Neeko','placeholder','placeholder',(SELECT id FROM games WHERE url_name='lol')),
    ('Talon','placeholder','placeholder',(SELECT id FROM games WHERE url_name='lol'));

INSERT INTO
    champions_roles (champion_id,role_id)
VALUES
    ((SELECT id FROM championS WHERE name = 'Ahri'),(SELECT id FROM roles WHERE name = 'mage')),
    ((SELECT id FROM championS WHERE name = 'Sivir'),(SELECT id FROM roles WHERE name = 'marksman')),
    ((SELECT id FROM championS WHERE name = 'Elise'),(SELECT id FROM roles WHERE name = 'mage')),
    ((SELECT id FROM championS WHERE name = 'Neeko'),(SELECT id FROM roles WHERE name = 'mage')),
    ((SELECT id FROM championS WHERE name = 'Talon'),(SELECT id FROM roles WHERE name = 'assassin'));

INSERT INTO
    positions (name,game_id)
VALUES 
    ('top',(SELECT id FROM games WHERE url_name = 'lol')),
    ('mid',(SELECT id FROM games WHERE url_name = 'lol')),
    ('jungle',(SELECT id FROM games WHERE url_name = 'lol')),
    ('support',(SELECT id FROM games WHERE url_name = 'lol')),
    ('bot',(SELECT id FROM games WHERE url_name = 'lol'));
