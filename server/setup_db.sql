-- Enabling UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Creating the table
CREATE TABLE data (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id BIGINT,
    chat_id BIGINT,
    prompt TEXT,
    natural_prompt TEXT,
    path_to_img TEXT,
    current_status INTEGER
);
