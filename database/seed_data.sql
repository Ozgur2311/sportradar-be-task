-- =========================
-- SEED DATA FOR SPORTRADAR TASK
-- =========================

-- SPORTS
INSERT INTO sports (id, name) VALUES (1, 'Football');
INSERT INTO sports (id, name) VALUES (2, 'Basketball');
INSERT INTO sports (id, name) VALUES (3, 'Volleyball');
INSERT INTO sports (id, name) VALUES (4, 'Baseball');

-- LEAGUES
INSERT INTO leagues (id, name, type, sport_id) VALUES (1, 'UEFA Champions League', 'Tournament', 1);
INSERT INTO leagues (id, name, type, sport_id) VALUES (2, 'Turkish Super Lig', 'League', 1);
INSERT INTO leagues (id, name, type, sport_id) VALUES (3, 'Premier League', 'League', 1);
INSERT INTO leagues (id, name, type, sport_id) VALUES (4, 'La Liga', 'League', 1);

INSERT INTO leagues (id, name, type, sport_id) VALUES (5, 'NBA', 'League', 2);
INSERT INTO leagues (id, name, type, sport_id) VALUES (6, 'EuroLeague', 'Tournament', 2);

INSERT INTO leagues (id, name, type, sport_id) VALUES (7, 'CEV Volleyball Cup Women', 'Tournament', 3);
INSERT INTO leagues (id, name, type, sport_id) VALUES (8, 'CEV Challenge Cup Men', 'Tournament', 3);
INSERT INTO leagues (id, name, type, sport_id) VALUES (9, 'Turkish Volleyball League', 'League', 3);
INSERT INTO leagues (id, name, type, sport_id) VALUES (10, 'Austrian Volleyball League', 'League', 3);
INSERT INTO leagues (id, name, type, sport_id) VALUES (11, 'CEV Champions League Women', 'Tournament', 3);

INSERT INTO leagues (id, name, type, sport_id) VALUES (12, 'MLB', 'League', 4);
INSERT INTO leagues (id, name, type, sport_id) VALUES (13, 'NPB', 'League', 4);
INSERT INTO leagues (id, name, type, sport_id) VALUES (14, 'Mexican League', 'League', 4);

-- TEAMS
INSERT INTO teams (id, name, city, country, sport_id) VALUES (1, 'Real Madrid', 'Madrid', 'Spain', 1);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (2, 'Bayern Munich', 'Munich', 'Germany', 1);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (3, 'Paris Saint-Germain', 'Paris', 'France', 1);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (4, 'Liverpool', 'Liverpool', 'England', 1);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (5, 'Fenerbahce', 'Istanbul', 'Turkey', 1);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (6, 'Besiktas', 'Istanbul', 'Turkey', 1);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (7, 'Manchester City', 'Manchester', 'England', 1);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (8, 'Arsenal', 'London', 'England', 1);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (9, 'Barcelona', 'Barcelona', 'Spain', 1);

INSERT INTO teams (id, name, city, country, sport_id) VALUES (10, 'Golden State Warriors', 'San Francisco', 'USA', 2);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (11, 'Houston Rockets', 'Houston', 'USA', 2);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (12, 'Los Angeles Lakers', 'Los Angeles', 'USA', 2);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (13, 'Oklahoma City Thunder', 'Oklahoma City', 'USA', 2);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (14, 'FC Barcelona', 'Barcelona', 'Spain', 2);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (15, 'Panathinaikos', 'Athens', 'Greece', 2);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (16, 'Anadolu Efes', 'Istanbul', 'Turkey', 2);

INSERT INTO teams (id, name, city, country, sport_id) VALUES (17, 'Chieri 76', 'Chieri', 'Italy', 3);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (18, 'Galatasaray Daikin', 'Istanbul', 'Turkey', 3);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (19, 'Allianz Milano', 'Milan', 'Italy', 3);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (20, 'Lindemans Aalst', 'Aalst', 'Belgium', 3);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (21, 'Halkbank Ankara', 'Ankara', 'Turkey', 3);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (22, 'Union Volleys', 'Vienna', 'Austria', 3);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (23, 'Wiener Volleyballverein', 'Vienna', 'Austria', 3);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (24, 'VakifBank', 'Istanbul', 'Turkey', 3);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (25, 'Imoco Conegliano', 'Conegliano', 'Italy', 3);

INSERT INTO teams (id, name, city, country, sport_id) VALUES (26, 'New York Yankees', 'New York', 'USA', 4);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (27, 'Miami Marlins', 'Miami', 'USA', 4);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (28, 'Detroit Tigers', 'Detroit', 'USA', 4);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (29, 'Chicago Cubs', 'Chicago', 'USA', 4);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (30, 'Pittsburgh Pirates', 'Pittsburgh', 'USA', 4);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (31, 'Orix Buffaloes', 'Osaka', 'Japan', 4);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (32, 'Saitama Seibu Lions', 'Saitama', 'Japan', 4);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (33, 'Olmecas de Tabasco', 'Villahermosa', 'Mexico', 4);
INSERT INTO teams (id, name, city, country, sport_id) VALUES (34, 'Tigres de Quintana Roo', 'Cancun', 'Mexico', 4);

-- VENUES
INSERT INTO venues (id, name, city, country) VALUES (1, 'Santiago Bernabeu', 'Madrid', 'Spain');
INSERT INTO venues (id, name, city, country) VALUES (2, 'Parc des Princes', 'Paris', 'France');
INSERT INTO venues (id, name, city, country) VALUES (3, 'Sukru Saracoglu Stadium', 'Istanbul', 'Turkey');
INSERT INTO venues (id, name, city, country) VALUES (4, 'Etihad Stadium', 'Manchester', 'England');
INSERT INTO venues (id, name, city, country) VALUES (5, 'Camp Nou', 'Barcelona', 'Spain');

INSERT INTO venues (id, name, city, country) VALUES (6, 'Chase Center', 'San Francisco', 'USA');
INSERT INTO venues (id, name, city, country) VALUES (7, 'Crypto.com Arena', 'Los Angeles', 'USA');
INSERT INTO venues (id, name, city, country) VALUES (8, 'Palau Blaugrana', 'Barcelona', 'Spain');
INSERT INTO venues (id, name, city, country) VALUES (9, 'OAKA Arena', 'Athens', 'Greece');

INSERT INTO venues (id, name, city, country) VALUES (10, 'Palafenera', 'Chieri', 'Italy');
INSERT INTO venues (id, name, city, country) VALUES (11, 'Allianz Cloud', 'Milan', 'Italy');
INSERT INTO venues (id, name, city, country) VALUES (12, 'Burhan Felek Vestel Volleyball Hall', 'Istanbul', 'Turkey');
INSERT INTO venues (id, name, city, country) VALUES (13, 'Volleyball Hall Vienna', 'Vienna', 'Austria');
INSERT INTO venues (id, name, city, country) VALUES (14, 'Ulker Sports Arena', 'Istanbul', 'Turkey');

INSERT INTO venues (id, name, city, country) VALUES (15, 'Yankee Stadium', 'New York', 'USA');
INSERT INTO venues (id, name, city, country) VALUES (16, 'Comerica Park', 'Detroit', 'USA');
INSERT INTO venues (id, name, city, country) VALUES (17, 'Wrigley Field', 'Chicago', 'USA');
INSERT INTO venues (id, name, city, country) VALUES (18, 'Kyocera Dome Osaka', 'Osaka', 'Japan');
INSERT INTO venues (id, name, city, country) VALUES (19, 'Centenario 27 de Febrero', 'Villahermosa', 'Mexico');

-- EVENTS
INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (1, 'Real Madrid vs Bayern Munich', DATE '2026-04-07', '22:00', 'UEFA Champions League quarter-final match.', 1, 1, 2, 1);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (2, 'Paris Saint-Germain vs Liverpool', DATE '2026-04-08', '22:00', 'UEFA Champions League quarter-final match.', 1, 3, 4, 2);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (3, 'Fenerbahce vs Besiktas', DATE '2026-04-05', '20:00', 'Turkish Super Lig derby match.', 2, 5, 6, 3);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (4, 'Manchester City vs Arsenal', DATE '2026-04-19', '18:30', 'Premier League top-tier match.', 3, 7, 8, 4);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (5, 'Barcelona vs Real Madrid', DATE '2026-05-10', '22:00', 'La Liga El Clasico match.', 4, 9, 1, 5);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (6, 'Golden State Warriors vs Houston Rockets', DATE '2026-04-06', '05:00', 'NBA regular season game.', 5, 10, 11, 6);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (7, 'Los Angeles Lakers vs Oklahoma City Thunder', DATE '2026-04-08', '05:30', 'NBA regular season game.', 5, 12, 13, 7);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (8, 'Golden State Warriors vs Los Angeles Lakers', DATE '2026-04-10', '05:00', 'NBA regular season rivalry game.', 5, 10, 12, 6);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (9, 'FC Barcelona vs Panathinaikos', DATE '2026-04-07', '21:30', 'EuroLeague regular season game.', 6, 14, 15, 8);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (10, 'Panathinaikos vs Anadolu Efes', DATE '2026-04-17', '21:15', 'EuroLeague regular season game.', 6, 15, 16, 9);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (11, 'Chieri 76 vs Galatasaray Daikin', DATE '2026-04-01', '21:00', 'CEV Volleyball Cup Women match.', 7, 17, 18, 10);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (12, 'Allianz Milano vs Lindemans Aalst', DATE '2026-04-01', '21:30', 'CEV Challenge Cup Men match.', 8, 19, 20, 11);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (13, 'Galatasaray Daikin vs Halkbank Ankara', DATE '2026-04-15', '19:00', 'Turkish Volleyball League match.', 9, 18, 21, 12);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (14, 'Union Volleys vs Wiener Volleyballverein', DATE '2026-04-18', '20:00', 'Austrian Volleyball League match.', 10, 22, 23, 13);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (15, 'VakifBank vs Imoco Conegliano', DATE '2026-05-02', '17:00', 'CEV Champions League Women match.', 11, 24, 25, 14);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (16, 'New York Yankees vs Miami Marlins', DATE '2026-04-03', '20:35', 'MLB regular season game.', 12, 26, 27, 15);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (17, 'Detroit Tigers vs Miami Marlins', DATE '2026-04-12', '20:40', 'MLB regular season game.', 12, 28, 27, 16);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (18, 'Chicago Cubs vs Pittsburgh Pirates', DATE '2026-04-12', '21:20', 'MLB regular season game.', 12, 29, 30, 17);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (19, 'Orix Buffaloes vs Saitama Seibu Lions', DATE '2026-04-15', '12:00', 'NPB regular season game.', 13, 31, 32, 18);

INSERT INTO events (id, title, event_date, event_time, description, league_id, home_team_id, away_team_id, venue_id)
VALUES (20, 'Olmecas de Tabasco vs Tigres de Quintana Roo', DATE '2026-04-19', '15:00', 'Mexican League regular season game.', 14, 33, 34, 19);

commit;