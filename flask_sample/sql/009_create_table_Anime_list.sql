CREATE TABLE
    IS601_Anime_list (
        id INT AUTO_INCREMENT PRIMARY KEY,
        anime_id int not null,
        user_id int not null,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY(anime_id) REFERENCES IS601_Anime(id),
        FOREIGN KEY(user_id) REFERENCES IS601_Users(id),
        UNIQUE KEY(anime_id, user_id)
    );