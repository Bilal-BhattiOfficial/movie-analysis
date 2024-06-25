-- DROP TABLE public.credits;
CREATE TABLE credits (
	person_id int4 NULL,
	id text NULL,
	"name" text NULL,
	"character" text NULL,
	"role" varchar(50) NULL
);

-- DROP TABLE public.ratings;
CREATE TABLE ratings (
	"ind" numeric NULL,
	id text NULL,
	title text NULL,
	"type" text NULL,
	description text NULL,
	release_year int4 NULL,
	age_certification text NULL,
	runtime numeric NULL,
	imdb_id text NULL,
	imdb_score numeric NULL,
	imdb_votes numeric NULL
);

-- DROP TABLE public.titles;
CREATE TABLE titles (
	id text NULL,
	title text NULL,
	"type" text NULL,
	description text NULL,
	release_year numeric NULL,
	age_certification text NULL,
	runtime numeric NULL,
	genres text NULL,
	production_countries text NULL,
	seasons numeric NULL,
	imdb_id text NULL,
	imdb_score numeric NULL,
	imdb_votes numeric NULL,
	tmdb_popularity numeric NULL,
	tmdb_score numeric NULL
);