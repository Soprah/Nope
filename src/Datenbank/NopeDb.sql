--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Karten; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Karten" (
    "Anzahl" integer NOT NULL,
    "Farbe" character varying,
    "Art" character varying,
    id integer
);


ALTER TABLE public."Karten" OWNER TO postgres;

--
-- Name: Spiel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Spiel" (
    "Id" integer NOT NULL,
    "Name" character varying,
    "Deck" character varying,
    "Spieler" integer
);


ALTER TABLE public."Spiel" OWNER TO postgres;

--
-- Name: Spieler; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Spieler" (
    "Id" integer NOT NULL,
    "Name" character varying,
    "Gegner" character varying,
    "Zug" boolean,
    "Hand" character varying
);


ALTER TABLE public."Spieler" OWNER TO postgres;

--
-- Name: Spielerstatistik; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Spielerstatistik" (
    "Id" integer NOT NULL,
    "Plazierung" integer,
    "Punkte" integer
);


ALTER TABLE public."Spielerstatistik" OWNER TO postgres;

--
-- Name: Spielplan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Spielplan" (
    "Id" integer NOT NULL,
    "Plan" character varying
);


ALTER TABLE public."Spielplan" OWNER TO postgres;

--
-- Name: Tabelle; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Tabelle" (
    "Id" integer NOT NULL,
    "Punktestand" character varying,
    "Plazierung" character varying
);


ALTER TABLE public."Tabelle" OWNER TO postgres;

--
-- Name: Karten Karten_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Karten"
    ADD CONSTRAINT "Karten_pkey" PRIMARY KEY ("Anzahl");


--
-- Name: Spiel Spiel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Spiel"
    ADD CONSTRAINT "Spiel_pkey" PRIMARY KEY ("Id");


--
-- Name: Spieler Spieler_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Spieler"
    ADD CONSTRAINT "Spieler_pkey" PRIMARY KEY ("Id");


--
-- Name: Spielerstatistik Spielerstatistik_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Spielerstatistik"
    ADD CONSTRAINT "Spielerstatistik_pkey" PRIMARY KEY ("Id");


--
-- Name: Spielplan Spielplan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Spielplan"
    ADD CONSTRAINT "Spielplan_pkey" PRIMARY KEY ("Id");


--
-- Name: Tabelle Tabelle_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Tabelle"
    ADD CONSTRAINT "Tabelle_pkey" PRIMARY KEY ("Id");


--
-- PostgreSQL database dump complete
--