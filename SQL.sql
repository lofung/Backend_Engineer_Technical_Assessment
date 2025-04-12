
CREATE TABLE necktie_categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);


CREATE TABLE necktie_districts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);


CREATE TABLE necktie_languages (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);


CREATE TABLE necktie_doctors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    category_id INT REFERENCES necktie_categories(id),
    district_id INT REFERENCES necktie_districts(id),
    price_range_low INT,
    price_range_high INT,
    languages JSONB, -- Store an array of language IDs for flexibility
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO necktie_categories (name) VALUES
('General Practitioner'),
('Pediatrician'),
('Dermatologist'),
('Cardiologist'),
('Orthopedic Surgeon'),
('Dentist'),
('Psychiatrist'),
('Gynecologist');


INSERT INTO necktie_districts (name) VALUES
('Central'),
('Tsim Sha Tsui'),
('Causeway Bay'),
('Mong Kok'),
('Wan Chai'),
('Kowloon'),
('Hong Kong Island'),
('Shatin'),
('Tsuen Wan');


INSERT INTO necktie_languages (name) VALUES
('Cantonese'),
('Mandarin'),
('English'),
('Spanish'),
('French'),
('Japanese'),
('Korean'),
('Tagalog');


INSERT INTO necktie_doctors (first_name, last_name, category_id, district_id, price_range_low, price_range_high, languages, bio) VALUES
('John', 'Smith', 1, 1, 300, 500, '["Cantonese", "English"]', 'Experienced general practitioner with over 10 years of practice in Hong Kong.'),
('Anna', 'Chan', 2, 2, 400, 600, '["Cantonese", "Mandarin"]', 'Pediatrician specializing in childhood diseases and vaccination schedules.'),
('Wong', 'Lee', 3, 3, 500, 700, '["Cantonese", "English"]', 'Certified dermatologist with expertise in skin conditions and cosmetic procedures.'),
('David', 'Ng', 4, 4, 700, 1200, '["English", "Mandarin"]', 'Cardiologist with over 15 years of experience in treating heart diseases.'),
('Samantha', 'Lau', 5, 5, 800, 1500, '["Cantonese", "English"]', 'Orthopedic surgeon specializing in joint replacement surgeries and sports injuries.'),
('Rachel', 'Ho', 6, 6, 400, 700, '["Cantonese", "English"]', 'Experienced dentist specializing in cosmetic and preventive dentistry.'),
('Michael', 'Cheng', 7, 7, 600, 900, '["English", "Cantonese"]', 'Psychiatrist with expertise in treating anxiety, depression, and stress-related disorders.'),
('Emily', 'Tan', 8, 8, 500, 800, '["Cantonese", "English"]', 'Gynecologist focusing on women\'s health, fertility, and prenatal care.'),
('Carlos', 'Garcia', 2, 9, 350, 550, '["Spanish", "English"]', 'Pediatrician with extensive experience in child nutrition and vaccinations.'),
('Yu', 'Ming', 4, 1, 600, 1000, '["Mandarin", "Cantonese"]', 'Cardiologist specializing in high blood pressure and heart failure treatments.');