--
-- PostgreSQL database dump
--

-- Dumped from database version 13.5
-- Dumped by pg_dump version 13.5

-- Started on 2022-02-28 12:26:31

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

DROP DATABASE bdnormativa;
--
-- TOC entry 3417 (class 1262 OID 43742)
-- Name: bdnormativa; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE bdnormativa WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Spain.1252';


ALTER DATABASE bdnormativa OWNER TO postgres;

\connect bdnormativa

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
-- TOC entry 200 (class 1259 OID 43743)
-- Name: apps_control_payment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.apps_control_payment (
    id integer NOT NULL,
    pay_method character varying(1) NOT NULL,
    pay_import numeric(10,2) NOT NULL,
    validity_date_start date NOT NULL,
    validity_date_finish date NOT NULL,
    register_date_time timestamp with time zone NOT NULL,
    id_plan_id integer,
    member_id integer
);


ALTER TABLE public.apps_control_payment OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 43746)
-- Name: apps_control_payment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.apps_control_payment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.apps_control_payment_id_seq OWNER TO postgres;

--
-- TOC entry 3418 (class 0 OID 0)
-- Dependencies: 201
-- Name: apps_control_payment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.apps_control_payment_id_seq OWNED BY public.apps_control_payment.id;


--
-- TOC entry 202 (class 1259 OID 43748)
-- Name: apps_member; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.apps_member (
    id integer NOT NULL,
    first_surname character varying(50) NOT NULL,
    second_surname character varying(50) NOT NULL,
    names character varying(50) NOT NULL,
    full_name character varying(200) NOT NULL,
    person_type character varying(1) NOT NULL,
    identity character varying(11) NOT NULL,
    profession character varying(1) NOT NULL,
    mobile character varying(12) NOT NULL,
    phone character varying(10) NOT NULL,
    email character varying(50) NOT NULL,
    tuition integer,
    secret_code integer,
    address character varying(200) NOT NULL,
    area_interest character varying(200) NOT NULL,
    institution character varying(200) NOT NULL,
    photo character varying(100),
    register_date_time timestamp with time zone NOT NULL,
    user_id integer,
    CONSTRAINT apps_member_secret_code_check CHECK ((secret_code >= 0)),
    CONSTRAINT apps_member_tuition_check CHECK ((tuition >= 0))
);


ALTER TABLE public.apps_member OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 43756)
-- Name: apps_member_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.apps_member_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.apps_member_id_seq OWNER TO postgres;

--
-- TOC entry 3419 (class 0 OID 0)
-- Dependencies: 203
-- Name: apps_member_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.apps_member_id_seq OWNED BY public.apps_member.id;


--
-- TOC entry 204 (class 1259 OID 43758)
-- Name: apps_plan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.apps_plan (
    id integer NOT NULL,
    planame character varying(200) NOT NULL,
    cost numeric(10,2) NOT NULL,
    validity_date_start date NOT NULL,
    validity_date_finish date NOT NULL,
    register_date_time date NOT NULL
);


ALTER TABLE public.apps_plan OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 43761)
-- Name: apps_plan_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.apps_plan_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.apps_plan_id_seq OWNER TO postgres;

--
-- TOC entry 3420 (class 0 OID 0)
-- Dependencies: 205
-- Name: apps_plan_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.apps_plan_id_seq OWNED BY public.apps_plan.id;


--
-- TOC entry 206 (class 1259 OID 43763)
-- Name: apps_policies_usage; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.apps_policies_usage (
    id integer NOT NULL,
    title character varying(200) NOT NULL,
    message text NOT NULL,
    platform character varying(1) NOT NULL,
    validity_date_start date NOT NULL,
    validity_date_finish date NOT NULL,
    register_date_time timestamp with time zone NOT NULL
);


ALTER TABLE public.apps_policies_usage OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 43769)
-- Name: apps_policies_usage_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.apps_policies_usage_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.apps_policies_usage_id_seq OWNER TO postgres;

--
-- TOC entry 3421 (class 0 OID 0)
-- Dependencies: 207
-- Name: apps_policies_usage_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.apps_policies_usage_id_seq OWNED BY public.apps_policies_usage.id;


--
-- TOC entry 208 (class 1259 OID 43771)
-- Name: apps_policies_usage_norma_name; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.apps_policies_usage_norma_name (
    id integer NOT NULL,
    policies_usage_id integer NOT NULL,
    master_normas_id bigint NOT NULL
);


ALTER TABLE public.apps_policies_usage_norma_name OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 43774)
-- Name: apps_policies_usage_norma_name_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.apps_policies_usage_norma_name_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.apps_policies_usage_norma_name_id_seq OWNER TO postgres;

--
-- TOC entry 3422 (class 0 OID 0)
-- Dependencies: 209
-- Name: apps_policies_usage_norma_name_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.apps_policies_usage_norma_name_id_seq OWNED BY public.apps_policies_usage_norma_name.id;


--
-- TOC entry 210 (class 1259 OID 43776)
-- Name: apps_usertoken; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.apps_usertoken (
    token uuid NOT NULL,
    user_profile_id integer NOT NULL
);


ALTER TABLE public.apps_usertoken OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 43779)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 43782)
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- TOC entry 3423 (class 0 OID 0)
-- Dependencies: 212
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- TOC entry 213 (class 1259 OID 43784)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 43787)
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 3424 (class 0 OID 0)
-- Dependencies: 214
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- TOC entry 215 (class 1259 OID 43789)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 43792)
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- TOC entry 3425 (class 0 OID 0)
-- Dependencies: 216
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- TOC entry 217 (class 1259 OID 43794)
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 43800)
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 43803)
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- TOC entry 3426 (class 0 OID 0)
-- Dependencies: 219
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- TOC entry 220 (class 1259 OID 43805)
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- TOC entry 3427 (class 0 OID 0)
-- Dependencies: 220
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- TOC entry 221 (class 1259 OID 43807)
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 43810)
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- TOC entry 3428 (class 0 OID 0)
-- Dependencies: 222
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- TOC entry 223 (class 1259 OID 43812)
-- Name: busqueda_normativa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.busqueda_normativa (
    id bigint NOT NULL,
    title character varying(150) NOT NULL,
    subtitle text NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.busqueda_normativa OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 43818)
-- Name: bus_normativa_date_normativa_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bus_normativa_date_normativa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bus_normativa_date_normativa_id_seq OWNER TO postgres;

--
-- TOC entry 3429 (class 0 OID 0)
-- Dependencies: 224
-- Name: bus_normativa_date_normativa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bus_normativa_date_normativa_id_seq OWNED BY public.busqueda_normativa.id;


--
-- TOC entry 225 (class 1259 OID 43820)
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 43827)
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- TOC entry 3430 (class 0 OID 0)
-- Dependencies: 226
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- TOC entry 227 (class 1259 OID 43829)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 43832)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- TOC entry 3431 (class 0 OID 0)
-- Dependencies: 228
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- TOC entry 229 (class 1259 OID 43834)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 43840)
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- TOC entry 3432 (class 0 OID 0)
-- Dependencies: 230
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- TOC entry 231 (class 1259 OID 43842)
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 43848)
-- Name: foro_categories_foro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.foro_categories_foro (
    id bigint NOT NULL,
    category_name character varying(200) NOT NULL,
    register_date_time timestamp with time zone NOT NULL
);


ALTER TABLE public.foro_categories_foro OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 43851)
-- Name: foro_categories_foro_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.foro_categories_foro_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.foro_categories_foro_id_seq OWNER TO postgres;

--
-- TOC entry 3433 (class 0 OID 0)
-- Dependencies: 233
-- Name: foro_categories_foro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.foro_categories_foro_id_seq OWNED BY public.foro_categories_foro.id;


--
-- TOC entry 234 (class 1259 OID 43853)
-- Name: foro_coments_foro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.foro_coments_foro (
    id bigint NOT NULL,
    coments character varying(200) NOT NULL,
    likes smallint NOT NULL,
    dislikes smallint NOT NULL,
    register_date_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    tema_id bigint,
    CONSTRAINT foro_coments_foro_dislikes_check CHECK ((dislikes >= 0)),
    CONSTRAINT foro_coments_foro_likes_check CHECK ((likes >= 0))
);


ALTER TABLE public.foro_coments_foro OWNER TO postgres;

--
-- TOC entry 235 (class 1259 OID 43858)
-- Name: foro_coments_foro_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.foro_coments_foro_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.foro_coments_foro_id_seq OWNER TO postgres;

--
-- TOC entry 3434 (class 0 OID 0)
-- Dependencies: 235
-- Name: foro_coments_foro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.foro_coments_foro_id_seq OWNED BY public.foro_coments_foro.id;


--
-- TOC entry 236 (class 1259 OID 43860)
-- Name: foro_subcategories_foro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.foro_subcategories_foro (
    id bigint NOT NULL,
    subcategory_name character varying(200) NOT NULL,
    register_date_time timestamp with time zone NOT NULL,
    categories_id bigint NOT NULL
);


ALTER TABLE public.foro_subcategories_foro OWNER TO postgres;

--
-- TOC entry 237 (class 1259 OID 43863)
-- Name: foro_subcategories_foro_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.foro_subcategories_foro_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.foro_subcategories_foro_id_seq OWNER TO postgres;

--
-- TOC entry 3435 (class 0 OID 0)
-- Dependencies: 237
-- Name: foro_subcategories_foro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.foro_subcategories_foro_id_seq OWNED BY public.foro_subcategories_foro.id;


--
-- TOC entry 238 (class 1259 OID 43865)
-- Name: foro_themas_foro; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.foro_themas_foro (
    id bigint NOT NULL,
    themas_name character varying(200) NOT NULL,
    register_date_time timestamp with time zone NOT NULL,
    subcategories_id bigint NOT NULL
);


ALTER TABLE public.foro_themas_foro OWNER TO postgres;

--
-- TOC entry 239 (class 1259 OID 43868)
-- Name: foro_themas_foro_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.foro_themas_foro_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.foro_themas_foro_id_seq OWNER TO postgres;

--
-- TOC entry 3436 (class 0 OID 0)
-- Dependencies: 239
-- Name: foro_themas_foro_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.foro_themas_foro_id_seq OWNED BY public.foro_themas_foro.id;


--
-- TOC entry 240 (class 1259 OID 43870)
-- Name: normas_areas_normas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.normas_areas_normas (
    id bigint NOT NULL,
    area_name character varying(200) NOT NULL,
    register_date_time timestamp with time zone NOT NULL,
    created timestamp with time zone,
    updated timestamp with time zone
);


ALTER TABLE public.normas_areas_normas OWNER TO postgres;

--
-- TOC entry 241 (class 1259 OID 43873)
-- Name: normas_areas_normas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.normas_areas_normas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.normas_areas_normas_id_seq OWNER TO postgres;

--
-- TOC entry 3437 (class 0 OID 0)
-- Dependencies: 241
-- Name: normas_areas_normas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.normas_areas_normas_id_seq OWNED BY public.normas_areas_normas.id;


--
-- TOC entry 242 (class 1259 OID 43875)
-- Name: normas_categories_normas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.normas_categories_normas (
    id bigint NOT NULL,
    category_name character varying(200) NOT NULL,
    register_date_time timestamp with time zone NOT NULL,
    created timestamp with time zone,
    updated timestamp with time zone
);


ALTER TABLE public.normas_categories_normas OWNER TO postgres;

--
-- TOC entry 243 (class 1259 OID 43878)
-- Name: normas_categories_normas_area_name; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.normas_categories_normas_area_name (
    id integer NOT NULL,
    categories_normas_id bigint NOT NULL,
    areas_normas_id bigint NOT NULL
);


ALTER TABLE public.normas_categories_normas_area_name OWNER TO postgres;

--
-- TOC entry 244 (class 1259 OID 43881)
-- Name: normas_categories_normas_area_name_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.normas_categories_normas_area_name_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.normas_categories_normas_area_name_id_seq OWNER TO postgres;

--
-- TOC entry 3438 (class 0 OID 0)
-- Dependencies: 244
-- Name: normas_categories_normas_area_name_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.normas_categories_normas_area_name_id_seq OWNED BY public.normas_categories_normas_area_name.id;


--
-- TOC entry 245 (class 1259 OID 43883)
-- Name: normas_categories_normas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.normas_categories_normas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.normas_categories_normas_id_seq OWNER TO postgres;

--
-- TOC entry 3439 (class 0 OID 0)
-- Dependencies: 245
-- Name: normas_categories_normas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.normas_categories_normas_id_seq OWNED BY public.normas_categories_normas.id;


--
-- TOC entry 246 (class 1259 OID 43885)
-- Name: normas_location_normas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.normas_location_normas (
    id bigint NOT NULL,
    "Location_name" character varying(200) NOT NULL,
    register_date_time timestamp with time zone NOT NULL,
    created timestamp with time zone,
    updated timestamp with time zone
);


ALTER TABLE public.normas_location_normas OWNER TO postgres;

--
-- TOC entry 247 (class 1259 OID 43888)
-- Name: normas_location_normas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.normas_location_normas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.normas_location_normas_id_seq OWNER TO postgres;

--
-- TOC entry 3440 (class 0 OID 0)
-- Dependencies: 247
-- Name: normas_location_normas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.normas_location_normas_id_seq OWNED BY public.normas_location_normas.id;


--
-- TOC entry 248 (class 1259 OID 43890)
-- Name: normas_master_normas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.normas_master_normas (
    id bigint NOT NULL,
    norma_rne character varying(50) NOT NULL,
    norma_name character varying(200) NOT NULL,
    validity_date_start date NOT NULL,
    keywords character varying(200) NOT NULL,
    file character varying(100) NOT NULL,
    register_date_time timestamp with time zone NOT NULL,
    area_name_id bigint NOT NULL,
    category_name_id bigint NOT NULL,
    location_name_id bigint NOT NULL,
    subcategory_name_id bigint NOT NULL,
    created timestamp with time zone,
    updated timestamp with time zone
);


ALTER TABLE public.normas_master_normas OWNER TO postgres;

--
-- TOC entry 249 (class 1259 OID 43896)
-- Name: normas_master_normas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.normas_master_normas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.normas_master_normas_id_seq OWNER TO postgres;

--
-- TOC entry 3441 (class 0 OID 0)
-- Dependencies: 249
-- Name: normas_master_normas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.normas_master_normas_id_seq OWNED BY public.normas_master_normas.id;


--
-- TOC entry 250 (class 1259 OID 43898)
-- Name: normas_subcategories_normas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.normas_subcategories_normas (
    id bigint NOT NULL,
    subcategory_name character varying(200) NOT NULL,
    register_date_time timestamp with time zone NOT NULL,
    created timestamp with time zone,
    "order" character varying(10) NOT NULL,
    updated timestamp with time zone
);


ALTER TABLE public.normas_subcategories_normas OWNER TO postgres;

--
-- TOC entry 251 (class 1259 OID 43901)
-- Name: normas_subcategories_normas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.normas_subcategories_normas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.normas_subcategories_normas_id_seq OWNER TO postgres;

--
-- TOC entry 3442 (class 0 OID 0)
-- Dependencies: 251
-- Name: normas_subcategories_normas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.normas_subcategories_normas_id_seq OWNED BY public.normas_subcategories_normas.id;


--
-- TOC entry 252 (class 1259 OID 43903)
-- Name: normas_subnormativa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.normas_subnormativa (
    id bigint NOT NULL,
    norma_sub_id bigint NOT NULL,
    norma character varying(200) NOT NULL,
    created timestamp with time zone,
    updated timestamp with time zone
);


ALTER TABLE public.normas_subnormativa OWNER TO postgres;

--
-- TOC entry 253 (class 1259 OID 43906)
-- Name: normas_subnormativa_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.normas_subnormativa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.normas_subnormativa_id_seq OWNER TO postgres;

--
-- TOC entry 3443 (class 0 OID 0)
-- Dependencies: 253
-- Name: normas_subnormativa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.normas_subnormativa_id_seq OWNED BY public.normas_subnormativa.id;


--
-- TOC entry 254 (class 1259 OID 43908)
-- Name: register_normativa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.register_normativa (
    id bigint NOT NULL,
    norma character varying(200) NOT NULL,
    name_denom text NOT NULL,
    base_legal character varying(200) NOT NULL,
    fecha_publi date NOT NULL,
    tipo_norma_id bigint,
    tipo_uso_id bigint,
    document character varying(100),
    created timestamp with time zone,
    descripcion character varying(200),
    es_foro boolean NOT NULL,
    es_vigente boolean NOT NULL,
    updated timestamp with time zone
);


ALTER TABLE public.register_normativa OWNER TO postgres;

--
-- TOC entry 255 (class 1259 OID 43914)
-- Name: register_normativa_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.register_normativa_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.register_normativa_id_seq OWNER TO postgres;

--
-- TOC entry 3444 (class 0 OID 0)
-- Dependencies: 255
-- Name: register_normativa_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.register_normativa_id_seq OWNED BY public.register_normativa.id;


--
-- TOC entry 256 (class 1259 OID 43916)
-- Name: register_palabclave; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.register_palabclave (
    id bigint NOT NULL,
    name character varying(200) NOT NULL,
    created timestamp with time zone,
    updated timestamp with time zone
);


ALTER TABLE public.register_palabclave OWNER TO postgres;

--
-- TOC entry 257 (class 1259 OID 43919)
-- Name: register_palabclave_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.register_palabclave_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.register_palabclave_id_seq OWNER TO postgres;

--
-- TOC entry 3445 (class 0 OID 0)
-- Dependencies: 257
-- Name: register_palabclave_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.register_palabclave_id_seq OWNED BY public.register_palabclave.id;


--
-- TOC entry 258 (class 1259 OID 43921)
-- Name: register_palabclave_normativas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.register_palabclave_normativas (
    id integer NOT NULL,
    register_palabraclave_id bigint NOT NULL,
    register_normativa_id bigint NOT NULL
);


ALTER TABLE public.register_palabclave_normativas OWNER TO postgres;

--
-- TOC entry 259 (class 1259 OID 43924)
-- Name: register_palabclave_normativas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.register_palabclave_normativas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.register_palabclave_normativas_id_seq OWNER TO postgres;

--
-- TOC entry 3446 (class 0 OID 0)
-- Dependencies: 259
-- Name: register_palabclave_normativas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.register_palabclave_normativas_id_seq OWNED BY public.register_palabclave_normativas.id;


--
-- TOC entry 3035 (class 2604 OID 43926)
-- Name: apps_control_payment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_control_payment ALTER COLUMN id SET DEFAULT nextval('public.apps_control_payment_id_seq'::regclass);


--
-- TOC entry 3036 (class 2604 OID 43927)
-- Name: apps_member id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_member ALTER COLUMN id SET DEFAULT nextval('public.apps_member_id_seq'::regclass);


--
-- TOC entry 3039 (class 2604 OID 43928)
-- Name: apps_plan id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_plan ALTER COLUMN id SET DEFAULT nextval('public.apps_plan_id_seq'::regclass);


--
-- TOC entry 3040 (class 2604 OID 43929)
-- Name: apps_policies_usage id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_policies_usage ALTER COLUMN id SET DEFAULT nextval('public.apps_policies_usage_id_seq'::regclass);


--
-- TOC entry 3041 (class 2604 OID 43930)
-- Name: apps_policies_usage_norma_name id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_policies_usage_norma_name ALTER COLUMN id SET DEFAULT nextval('public.apps_policies_usage_norma_name_id_seq'::regclass);


--
-- TOC entry 3042 (class 2604 OID 43931)
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- TOC entry 3043 (class 2604 OID 43932)
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- TOC entry 3044 (class 2604 OID 43933)
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- TOC entry 3045 (class 2604 OID 43934)
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- TOC entry 3046 (class 2604 OID 43935)
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- TOC entry 3047 (class 2604 OID 43936)
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- TOC entry 3048 (class 2604 OID 43937)
-- Name: busqueda_normativa id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.busqueda_normativa ALTER COLUMN id SET DEFAULT nextval('public.bus_normativa_date_normativa_id_seq'::regclass);


--
-- TOC entry 3049 (class 2604 OID 43938)
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- TOC entry 3051 (class 2604 OID 43939)
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- TOC entry 3052 (class 2604 OID 43940)
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- TOC entry 3053 (class 2604 OID 43941)
-- Name: foro_categories_foro id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foro_categories_foro ALTER COLUMN id SET DEFAULT nextval('public.foro_categories_foro_id_seq'::regclass);


--
-- TOC entry 3054 (class 2604 OID 43942)
-- Name: foro_coments_foro id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foro_coments_foro ALTER COLUMN id SET DEFAULT nextval('public.foro_coments_foro_id_seq'::regclass);


--
-- TOC entry 3057 (class 2604 OID 43943)
-- Name: foro_subcategories_foro id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foro_subcategories_foro ALTER COLUMN id SET DEFAULT nextval('public.foro_subcategories_foro_id_seq'::regclass);


--
-- TOC entry 3058 (class 2604 OID 43944)
-- Name: foro_themas_foro id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foro_themas_foro ALTER COLUMN id SET DEFAULT nextval('public.foro_themas_foro_id_seq'::regclass);


--
-- TOC entry 3059 (class 2604 OID 43945)
-- Name: normas_areas_normas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_areas_normas ALTER COLUMN id SET DEFAULT nextval('public.normas_areas_normas_id_seq'::regclass);


--
-- TOC entry 3060 (class 2604 OID 43946)
-- Name: normas_categories_normas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_categories_normas ALTER COLUMN id SET DEFAULT nextval('public.normas_categories_normas_id_seq'::regclass);


--
-- TOC entry 3061 (class 2604 OID 43947)
-- Name: normas_categories_normas_area_name id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_categories_normas_area_name ALTER COLUMN id SET DEFAULT nextval('public.normas_categories_normas_area_name_id_seq'::regclass);


--
-- TOC entry 3062 (class 2604 OID 43948)
-- Name: normas_location_normas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_location_normas ALTER COLUMN id SET DEFAULT nextval('public.normas_location_normas_id_seq'::regclass);


--
-- TOC entry 3063 (class 2604 OID 43949)
-- Name: normas_master_normas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_master_normas ALTER COLUMN id SET DEFAULT nextval('public.normas_master_normas_id_seq'::regclass);


--
-- TOC entry 3064 (class 2604 OID 43950)
-- Name: normas_subcategories_normas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_subcategories_normas ALTER COLUMN id SET DEFAULT nextval('public.normas_subcategories_normas_id_seq'::regclass);


--
-- TOC entry 3065 (class 2604 OID 43951)
-- Name: normas_subnormativa id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_subnormativa ALTER COLUMN id SET DEFAULT nextval('public.normas_subnormativa_id_seq'::regclass);


--
-- TOC entry 3066 (class 2604 OID 43952)
-- Name: register_normativa id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.register_normativa ALTER COLUMN id SET DEFAULT nextval('public.register_normativa_id_seq'::regclass);


--
-- TOC entry 3067 (class 2604 OID 43953)
-- Name: register_palabclave id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.register_palabclave ALTER COLUMN id SET DEFAULT nextval('public.register_palabclave_id_seq'::regclass);


--
-- TOC entry 3068 (class 2604 OID 43954)
-- Name: register_palabclave_normativas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.register_palabclave_normativas ALTER COLUMN id SET DEFAULT nextval('public.register_palabclave_normativas_id_seq'::regclass);


--
-- TOC entry 3352 (class 0 OID 43743)
-- Dependencies: 200
-- Data for Name: apps_control_payment; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3354 (class 0 OID 43748)
-- Dependencies: 202
-- Data for Name: apps_member; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.apps_member (id, first_surname, second_surname, names, full_name, person_type, identity, profession, mobile, phone, email, tuition, secret_code, address, area_interest, institution, photo, register_date_time, user_id) VALUES (1, 'VILLEGAS', 'PACHECO', 'ANDREA GIULIANA', 'Nombre completo', 'N', '73684340', 'A', '935863306', '017809960', 'avillegas@dt-data.com', 789, 1234, 'av.san jose 123', '', '', '', '2022-02-23 15:04:58.134334-05', NULL);
INSERT INTO public.apps_member (id, first_surname, second_surname, names, full_name, person_type, identity, profession, mobile, phone, email, tuition, secret_code, address, area_interest, institution, photo, register_date_time, user_id) VALUES (3, 'user1', 'user1', 'user1', 'Nombre completo', 'N', '83928194', 'A', '923678387', '333333', 'suyon.jesus@gmail.com', 2000, 22, 'k3jmkm', '', '', '', '2022-02-23 16:56:14.923323-05', NULL);


--
-- TOC entry 3356 (class 0 OID 43758)
-- Dependencies: 204
-- Data for Name: apps_plan; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3358 (class 0 OID 43763)
-- Dependencies: 206
-- Data for Name: apps_policies_usage; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3360 (class 0 OID 43771)
-- Dependencies: 208
-- Data for Name: apps_policies_usage_norma_name; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3362 (class 0 OID 43776)
-- Dependencies: 210
-- Data for Name: apps_usertoken; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3363 (class 0 OID 43779)
-- Dependencies: 211
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_group (id, name) VALUES (1, 'Premium');
INSERT INTO public.auth_group (id, name) VALUES (2, 'Profesional');
INSERT INTO public.auth_group (id, name) VALUES (3, 'Gratuito');


--
-- TOC entry 3365 (class 0 OID 43784)
-- Dependencies: 213
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (1, 1, 1);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (2, 1, 2);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (3, 1, 3);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (4, 1, 4);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (5, 1, 5);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (6, 1, 6);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (7, 1, 7);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (8, 1, 8);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (9, 1, 9);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (10, 1, 10);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (11, 1, 11);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (12, 1, 12);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (13, 1, 13);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (14, 1, 14);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (15, 1, 15);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (16, 1, 16);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (17, 1, 17);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (18, 1, 18);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (19, 1, 19);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (20, 1, 20);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (21, 1, 21);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (22, 1, 22);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (23, 1, 23);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (24, 1, 24);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (25, 1, 25);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (26, 1, 26);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (27, 1, 27);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (28, 1, 28);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (29, 1, 29);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (30, 1, 30);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (31, 1, 31);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (32, 1, 32);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (33, 1, 33);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (34, 1, 34);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (35, 1, 35);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (36, 1, 36);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (37, 1, 37);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (38, 1, 38);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (39, 1, 39);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (40, 1, 40);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (41, 1, 41);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (42, 1, 42);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (43, 1, 43);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (44, 1, 44);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (45, 1, 45);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (46, 1, 46);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (47, 1, 47);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (48, 1, 48);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (49, 1, 49);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (50, 1, 50);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (51, 1, 51);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (52, 1, 52);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (53, 1, 53);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (54, 1, 54);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (55, 1, 55);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (56, 1, 56);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (57, 1, 57);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (58, 1, 58);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (59, 1, 59);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (60, 1, 60);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (61, 1, 61);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (62, 1, 62);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (63, 1, 63);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (64, 1, 64);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (65, 1, 65);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (66, 1, 66);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (67, 1, 67);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (68, 1, 68);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (69, 1, 69);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (70, 1, 70);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (71, 1, 71);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (72, 1, 72);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (73, 1, 73);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (74, 1, 74);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (75, 1, 75);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (76, 1, 76);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (77, 1, 77);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (78, 1, 78);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (79, 1, 79);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (80, 1, 80);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (81, 1, 81);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (82, 1, 82);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (83, 1, 83);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (84, 1, 84);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (85, 1, 85);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (86, 1, 86);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (87, 1, 87);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (88, 1, 88);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (89, 1, 89);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (90, 1, 90);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (91, 1, 91);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (92, 1, 92);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (93, 1, 93);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (94, 1, 94);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (95, 1, 95);
INSERT INTO public.auth_group_permissions (id, group_id, permission_id) VALUES (96, 1, 96);


--
-- TOC entry 3367 (class 0 OID 43789)
-- Dependencies: 215
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (25, 'Can add member', 7, 'add_member');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (26, 'Can change member', 7, 'change_member');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (27, 'Can delete member', 7, 'delete_member');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (28, 'Can view member', 7, 'view_member');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (29, 'Can add plan', 8, 'add_plan');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (30, 'Can change plan', 8, 'change_plan');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (31, 'Can delete plan', 8, 'delete_plan');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (32, 'Can view plan', 8, 'view_plan');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (33, 'Can add user token', 9, 'add_usertoken');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (34, 'Can change user token', 9, 'change_usertoken');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (35, 'Can delete user token', 9, 'delete_usertoken');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (36, 'Can view user token', 9, 'view_usertoken');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (37, 'Can add policies_usage', 10, 'add_policies_usage');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (38, 'Can change policies_usage', 10, 'change_policies_usage');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (39, 'Can delete policies_usage', 10, 'delete_policies_usage');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (40, 'Can view policies_usage', 10, 'view_policies_usage');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (41, 'Can add control_payment', 11, 'add_control_payment');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (42, 'Can change control_payment', 11, 'change_control_payment');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (43, 'Can delete control_payment', 11, 'delete_control_payment');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (44, 'Can view control_payment', 11, 'view_control_payment');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (45, 'Can add categories_foro', 12, 'add_categories_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (46, 'Can change categories_foro', 12, 'change_categories_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (47, 'Can delete categories_foro', 12, 'delete_categories_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (48, 'Can view categories_foro', 12, 'view_categories_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (49, 'Can add subcategories_foro', 13, 'add_subcategories_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (50, 'Can change subcategories_foro', 13, 'change_subcategories_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (51, 'Can delete subcategories_foro', 13, 'delete_subcategories_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (52, 'Can view subcategories_foro', 13, 'view_subcategories_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (53, 'Can add themas_foro', 14, 'add_themas_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (54, 'Can change themas_foro', 14, 'change_themas_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (55, 'Can delete themas_foro', 14, 'delete_themas_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (56, 'Can view themas_foro', 14, 'view_themas_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (57, 'Can add coments_foro', 15, 'add_coments_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (58, 'Can change coments_foro', 15, 'change_coments_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (59, 'Can delete coments_foro', 15, 'delete_coments_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (60, 'Can view coments_foro', 15, 'view_coments_foro');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (61, 'Can add areas_ normas', 16, 'add_areas_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (62, 'Can change areas_ normas', 16, 'change_areas_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (63, 'Can delete areas_ normas', 16, 'delete_areas_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (64, 'Can view areas_ normas', 16, 'view_areas_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (65, 'Can add categories_ normas', 17, 'add_categories_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (66, 'Can change categories_ normas', 17, 'change_categories_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (67, 'Can delete categories_ normas', 17, 'delete_categories_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (68, 'Can view categories_ normas', 17, 'view_categories_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (69, 'Can add location_ normas', 18, 'add_location_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (70, 'Can change location_ normas', 18, 'change_location_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (71, 'Can delete location_ normas', 18, 'delete_location_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (72, 'Can view location_ normas', 18, 'view_location_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (73, 'Can add register_ normativa', 19, 'add_register_normativa');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (74, 'Can change register_ normativa', 19, 'change_register_normativa');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (75, 'Can delete register_ normativa', 19, 'delete_register_normativa');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (76, 'Can view register_ normativa', 19, 'view_register_normativa');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (77, 'Can add subcategories_ normas', 20, 'add_subcategories_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (78, 'Can change subcategories_ normas', 20, 'change_subcategories_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (79, 'Can delete subcategories_ normas', 20, 'delete_subcategories_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (80, 'Can view subcategories_ normas', 20, 'view_subcategories_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (81, 'Can add sub normativa', 21, 'add_subnormativa');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (82, 'Can change sub normativa', 21, 'change_subnormativa');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (83, 'Can delete sub normativa', 21, 'delete_subnormativa');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (84, 'Can view sub normativa', 21, 'view_subnormativa');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (85, 'Can add register_ palabraclave', 22, 'add_register_palabraclave');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (86, 'Can change register_ palabraclave', 22, 'change_register_palabraclave');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (87, 'Can delete register_ palabraclave', 22, 'delete_register_palabraclave');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (88, 'Can view register_ palabraclave', 22, 'view_register_palabraclave');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (89, 'Can add master_ normas', 23, 'add_master_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (90, 'Can change master_ normas', 23, 'change_master_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (91, 'Can delete master_ normas', 23, 'delete_master_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (92, 'Can view master_ normas', 23, 'view_master_normas');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (93, 'Can add date_normativa', 24, 'add_date_normativa');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (94, 'Can change date_normativa', 24, 'change_date_normativa');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (95, 'Can delete date_normativa', 24, 'delete_date_normativa');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (96, 'Can view date_normativa', 24, 'view_date_normativa');


--
-- TOC entry 3369 (class 0 OID 43794)
-- Dependencies: 217
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (2, 'pbkdf2_sha256$260000$nQxFFQgzpSKYqKOh3yR5OX$KLUYDJQvW8xkG/FA6sD7qy69HYTrXqKvb5x7RnegSIc=', '2022-02-23 15:06:37.249871-05', false, '789', '', 'VILLEGAS', 'avillegas@dt-data.com', false, true, '2022-02-23 15:04:58.162346-05');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1, 'pbkdf2_sha256$260000$XRGIXI5BUrrutsxPbrxfBw$GNEUDNOXDwqRMMqhveAugEaBFR2RgKfKpRyOpe+URQM=', '2022-02-25 16:08:51.102533-05', true, 'jaime', 'Jaime', 'Marston', 'jaime@gmail.com', true, true, '2022-02-23 09:01:30-05');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (4, 'pbkdf2_sha256$260000$fABGEJ4YT9gflkg69ZoSAO$mUiVTFhBZ4eMvZfHF1jyUOh5LDoApIsFNyVxCvH2dM8=', '2022-02-23 16:56:32.136343-05', false, '2000', '', 'user1', 'suyon.jesus@gmail.com', false, true, '2022-02-23 16:56:14.929374-05');


--
-- TOC entry 3370 (class 0 OID 43800)
-- Dependencies: 218
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (1, 1, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (2, 2, 3);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (4, 4, 3);


--
-- TOC entry 3373 (class 0 OID 43807)
-- Dependencies: 221
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3375 (class 0 OID 43812)
-- Dependencies: 223
-- Data for Name: busqueda_normativa; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3377 (class 0 OID 43820)
-- Dependencies: 225
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (1, '2022-02-23 09:02:39.099983-05', '1', 'Premium', 1, '[{"added": {}}]', 3, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (2, '2022-02-23 09:02:54.39007-05', '1', 'jaime', 2, '[{"changed": {"fields": ["Groups"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (3, '2022-02-23 09:03:08.400948-05', '2', 'Profesional', 1, '[{"added": {}}]', 3, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (4, '2022-02-23 09:03:22.599453-05', '3', 'Gratuito', 1, '[{"added": {}}]', 3, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (5, '2022-02-23 09:04:41.999042-05', '1', 'VIVIENDA', 1, '[{"added": {}}]', 16, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (6, '2022-02-23 09:05:01.670882-05', '1', 'RNE', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (7, '2022-02-23 09:41:13.483228-05', '1', '1. RNE', 2, '[{"changed": {"fields": ["Sub Categoria"]}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (8, '2022-02-23 09:41:27.33071-05', '2', '1.1 Arquitectura', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (9, '2022-02-23 09:41:55.790763-05', '3', '1.1.1 TRANSVERSALES', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (10, '2022-02-23 09:42:05.320794-05', '4', '1.1.2 VIVIENDA', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (11, '2022-02-23 09:42:26.023977-05', '5', '1.2 ESPECIALIDADES RELACIONADAS', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (12, '2022-02-23 09:42:40.755857-05', '6', '2.NORMAS SECTORIALES', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (13, '2022-02-23 09:42:55.089214-05', '7', '2.1 GAS VIVIENDAS ENERGIA Y MINAS', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (14, '2022-02-23 09:43:05.923364-05', '8', '2.2 RATDUS-Ministerio de Vivienda', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (15, '2022-02-23 09:43:18.570144-05', '9', '2.3 VIVIENDA DE INTERES SOCIAL- MIN. DE VIVIENDA', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (16, '2022-02-23 09:43:47.506979-05', '10', '3.OPINIONES VINCULANTES', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (17, '2022-02-23 09:44:00.864059-05', '1', '1. RNE', 2, '[{"changed": {"fields": ["Order"]}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (18, '2022-02-23 09:44:08.629919-05', '2', '1.1 Arquitectura', 2, '[{"changed": {"fields": ["Order"]}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (19, '2022-02-23 09:44:19.095589-05', '3', '1.1.1 TRANSVERSALES', 2, '[{"changed": {"fields": ["Order"]}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (20, '2022-02-23 09:44:29.233011-05', '4', '1.1.2 VIVIENDA', 2, '[{"changed": {"fields": ["Order"]}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (21, '2022-02-23 09:44:47.494795-05', '6', '2.NORMAS SECTORIALES', 2, '[{"changed": {"fields": ["Order"]}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (22, '2022-02-23 09:45:03.859942-05', '1', '1. RNE', 2, '[{"changed": {"fields": ["Order"]}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (23, '2022-02-23 09:45:12.753011-05', '6', '2.NORMAS SECTORIALES', 2, '[{"changed": {"fields": ["Order"]}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (24, '2022-02-23 09:45:20.208429-05', '10', '3.OPINIONES VINCULANTES', 2, '[{"changed": {"fields": ["Order"]}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (25, '2022-02-23 09:45:29.211745-05', '5', '1.2 ESPECIALIDADES RELACIONADAS', 2, '[{"changed": {"fields": ["Order"]}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (26, '2022-02-23 09:45:51.396174-05', '7', '2.1 GAS VIVIENDAS ENERGIA Y MINAS', 2, '[{"changed": {"fields": ["Order"]}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (27, '2022-02-23 09:46:01.575062-05', '8', '2.2 RATDUS-Ministerio de Vivienda', 2, '[{"changed": {"fields": ["Order"]}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (28, '2022-02-23 09:46:12.497012-05', '9', '2.3 VIVIENDA DE INTERES SOCIAL- MIN. DE VIVIENDA', 2, '[{"changed": {"fields": ["Order"]}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (29, '2022-02-23 09:47:30.683914-05', '11', '3.1 VIVIENDA DE INTERES SOCIAL- MIN. DE VIVIENDA', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (30, '2022-02-23 09:47:39.26637-05', '12', '4.REGLAMENTO COMENTADO', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (31, '2022-02-23 09:47:55.568421-05', '13', '4.1 NORMA GRAFICA COMENTADA', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (32, '2022-02-23 09:48:07.030624-05', '14', '4.2 CASUISTICA', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (33, '2022-02-23 09:48:14.543877-05', '15', '4.2.1 APELACIONES RECONSIDERACIONES', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (34, '2022-02-23 09:48:29.523677-05', '16', '4.2.2 CONCLUSIONES DE CHARLAS(OPINION DE ASUNTOS TECNICOS )', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (35, '2022-02-23 09:48:36.657091-05', '17', '4.2.3 DIRECTIVAS CAP', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (36, '2022-02-23 09:48:48.840559-05', '18', '5.INDECOPI', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (37, '2022-02-23 09:48:57.140912-05', '19', '6.NORMAS MUNICIPALES', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (38, '2022-02-23 09:49:05.245294-05', '20', '6.1 NORMAS PROVINCIALES', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (39, '2022-02-23 09:49:11.309936-05', '21', '6.2 NORMAS DISTRITALES', 1, '[{"added": {}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (40, '2022-02-23 09:50:00.392044-05', '1', 'jaime', 2, '[{"changed": {"fields": ["First name", "Last name"]}}]', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (41, '2022-02-23 09:57:31.646346-05', '2', '1.1 RNE-ARQUITECTURA', 2, '[{"changed": {"fields": ["Sub Categoria"]}}]', 20, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (42, '2022-02-23 16:54:41.543751-05', '3', '1000', 3, '', 4, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (43, '2022-02-23 16:54:57.460087-05', '2', 'Nombre completo', 3, '', 7, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (44, '2022-02-23 18:03:06.006733-05', '2', 'resta', 1, '[{"added": {}}]', 16, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (45, '2022-02-23 18:03:15.746964-05', '2', 'resta', 3, '', 16, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (46, '2022-02-23 18:03:24.314832-05', '3', 'RESTAURANTES', 1, '[{"added": {}}]', 16, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (47, '2022-02-24 23:20:42.194109-05', '36', 'Centro Poblado', 2, '[{"changed": {"fields": ["Normativa"]}}]', 22, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (48, '2022-02-24 23:27:30.065967-05', '37', 'Edificación', 2, '[{"changed": {"fields": ["Normativa"]}}]', 22, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (49, '2022-02-25 16:00:04.953887-05', '16', 'Register_Normativa object (16)', 2, '[{"changed": {"fields": ["Denominacion", "Documentos"]}}]', 19, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (50, '2022-02-25 16:05:23.923626-05', '1', 'Register_Normativa object (1)', 2, '[{"changed": {"fields": ["Documentos"]}}]', 19, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (51, '2022-02-25 16:05:47.307393-05', '2', 'Register_Normativa object (2)', 2, '[{"changed": {"fields": ["Documentos"]}}]', 19, 1);


--
-- TOC entry 3379 (class 0 OID 43829)
-- Dependencies: 227
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_content_type (id, app_label, model) VALUES (1, 'admin', 'logentry');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (2, 'auth', 'permission');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (3, 'auth', 'group');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (4, 'auth', 'user');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (6, 'sessions', 'session');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (7, 'apps', 'member');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (8, 'apps', 'plan');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (9, 'apps', 'usertoken');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (10, 'apps', 'policies_usage');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (11, 'apps', 'control_payment');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (12, 'foro', 'categories_foro');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (13, 'foro', 'subcategories_foro');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (14, 'foro', 'themas_foro');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (15, 'foro', 'coments_foro');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (16, 'normas', 'areas_normas');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (17, 'normas', 'categories_normas');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (18, 'normas', 'location_normas');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (19, 'normas', 'register_normativa');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (20, 'normas', 'subcategories_normas');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (21, 'normas', 'subnormativa');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (22, 'normas', 'register_palabraclave');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (23, 'normas', 'master_normas');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (24, 'bus_normativa', 'date_normativa');


--
-- TOC entry 3381 (class 0 OID 43834)
-- Dependencies: 229
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_migrations (id, app, name, applied) VALUES (1, 'contenttypes', '0001_initial', '2022-02-23 09:00:51.148655-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (2, 'auth', '0001_initial', '2022-02-23 09:00:51.294186-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (3, 'admin', '0001_initial', '2022-02-23 09:00:51.325491-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2022-02-23 09:00:51.335641-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2022-02-23 09:00:51.344889-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (6, 'normas', '0001_initial', '2022-02-23 09:00:51.471512-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (7, 'apps', '0001_initial', '2022-02-23 09:00:51.606282-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (8, 'apps', '0002_alter_member_email', '2022-02-23 09:00:51.622755-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (9, 'contenttypes', '0002_remove_content_type_name', '2022-02-23 09:00:51.665487-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (10, 'auth', '0002_alter_permission_name_max_length', '2022-02-23 09:00:51.683967-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (11, 'auth', '0003_alter_user_email_max_length', '2022-02-23 09:00:51.700481-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (12, 'auth', '0004_alter_user_username_opts', '2022-02-23 09:00:51.715772-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (13, 'auth', '0005_alter_user_last_login_null', '2022-02-23 09:00:51.73249-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (14, 'auth', '0006_require_contenttypes_0002', '2022-02-23 09:00:51.737583-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (15, 'auth', '0007_alter_validators_add_error_messages', '2022-02-23 09:00:51.75499-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (16, 'auth', '0008_alter_user_username_max_length', '2022-02-23 09:00:51.779932-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (17, 'auth', '0009_alter_user_last_name_max_length', '2022-02-23 09:00:51.793576-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (18, 'auth', '0010_alter_group_name_max_length', '2022-02-23 09:00:51.817345-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (19, 'auth', '0011_update_proxy_permissions', '2022-02-23 09:00:51.844316-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (20, 'auth', '0012_alter_user_first_name_max_length', '2022-02-23 09:00:51.87309-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (21, 'bus_normativa', '0001_initial', '2022-02-23 09:00:51.889259-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (22, 'bus_normativa', '0002_alter_date_normativa_table', '2022-02-23 09:00:51.89828-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (23, 'normas', '0002_auto_20220223_0900', '2022-02-23 09:00:52.271661-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (24, 'foro', '0001_initial', '2022-02-23 09:00:52.349226-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (25, 'foro', '0002_auto_20220223_0900', '2022-02-23 09:00:52.410098-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (26, 'sessions', '0001_initial', '2022-02-23 09:00:52.43663-05');


--
-- TOC entry 3383 (class 0 OID 43842)
-- Dependencies: 231
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('is0fzah84upzil7x59zonmgiyfvya3pq', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nMwsE:Uni2s7MAyx30jJPfp3c4pKhqP7LZRoEPn4DP0L3hKzg', '2022-03-09 14:00:26.777911-05');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('s8og7rvuxxp5fbqsvltoco3q37g0fjvt', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nMz2S:J3nirk50NRzFFZxnt7bwkSulUGTfhIiDxgpzB1LQl8Y', '2022-03-09 16:19:08.414858-05');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('okhxzbb4rbgcw9wwajyvcqsuyeppd5sm', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nN0Cq:UEkYX4x3YpS-6yiPlk3ofadgIm7cy7h1fo4NM2n__EE', '2022-03-09 17:33:56.696031-05');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('e0ub5qlkh5zr7r8m05x0h4ch6ewykrbb', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nN0Gg:uAnuuKn3fgWXEWGDDCpCPLkw249miGrwhu8h_g-aiB0', '2022-03-09 17:37:54.393027-05');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('fgtwd01cc0y7hkm08g3tzk6aymmmuidb', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nNK1m:jWQhlW-qhosrT--6JvcOHSg5ZYb_S86FuYrp8FP3Pj0', '2022-03-10 14:43:50.763289-05');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('bwf8oluzbkkbk18wlsmxsiujv9g79xmd', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nNKFp:tF9VydgQUA09d5bLLTb3HLhMNdaDajxqiWnJL3Y6gTw', '2022-03-10 14:58:21.103368-05');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('xkozinx4j0ey5ez7fptpisjkeicv1ip6', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nNKyP:fPbqZYQOnYOJfLBGy3eGQtg3GbGLhFI8hK_UbAzK-18', '2022-03-10 15:44:25.828084-05');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('5omb0t78nam3ugqetlf5ygupzgf4djiw', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nNLHQ:GWGJqCP4mRWgYR63uD2S7BM7IUU1Qn_CqvGi8lOqE4I', '2022-03-10 16:04:04.524428-05');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('mls2576nbn110qs9hfu7aygbqlwkldup', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nNLWm:62ygxnilrdiQa1Q8BOm96t58leyOkJS5ooEcArWUZJA', '2022-03-10 16:19:56.830905-05');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('wq0gv87p9gsm1bdxji2khpvx0b4l3k79', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nNLbr:x3umDD6LOMxjdqnslo0DpbOkmgyIg3voB2WAZUtz_Wc', '2022-03-10 16:25:11.666405-05');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('1918ko8jj49s3s4tji39ubtiawc5en7x', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nNbKs:VjBBot0uh9dCdd0Evlw6TyoS8LwTCHjoX-_mByuDDnY', '2022-03-11 09:12:42.017964-05');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('6k6pwt6kjt3plz91cpe3vfepm84xwqi8', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nNeGv:B-vNECXU4qYRg1Y5U23oEw9KUaKW4Wk1bj2lGFYaqng', '2022-03-11 12:20:49.779404-05');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('7nz2b63bpudp96qa3rjm66d3z90wdmc2', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nNhpb:JeCKLzb-jLpEnTcdkAox9fziFYaCAQ0Vlch2PZ0uMTA', '2022-03-11 16:08:51.106258-05');


--
-- TOC entry 3384 (class 0 OID 43848)
-- Dependencies: 232
-- Data for Name: foro_categories_foro; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3386 (class 0 OID 43853)
-- Dependencies: 234
-- Data for Name: foro_coments_foro; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.foro_coments_foro (id, coments, likes, dislikes, register_date_time, user_id, tema_id) VALUES (1, 'un comentario', 0, 0, '2022-02-23 09:06:48.524386-05', 1, 1);


--
-- TOC entry 3388 (class 0 OID 43860)
-- Dependencies: 236
-- Data for Name: foro_subcategories_foro; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3390 (class 0 OID 43865)
-- Dependencies: 238
-- Data for Name: foro_themas_foro; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3392 (class 0 OID 43870)
-- Dependencies: 240
-- Data for Name: normas_areas_normas; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.normas_areas_normas (id, area_name, register_date_time, created, updated) VALUES (1, 'VIVIENDA', '2022-02-23 09:04:41.996554-05', '2022-02-23 09:04:41.996568-05', '2022-02-23 09:04:41.996572-05');
INSERT INTO public.normas_areas_normas (id, area_name, register_date_time, created, updated) VALUES (3, 'RESTAURANTES', '2022-02-23 18:03:24.311788-05', '2022-02-23 18:03:24.311808-05', '2022-02-23 18:03:24.311815-05');


--
-- TOC entry 3394 (class 0 OID 43875)
-- Dependencies: 242
-- Data for Name: normas_categories_normas; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3395 (class 0 OID 43878)
-- Dependencies: 243
-- Data for Name: normas_categories_normas_area_name; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3398 (class 0 OID 43885)
-- Dependencies: 246
-- Data for Name: normas_location_normas; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3400 (class 0 OID 43890)
-- Dependencies: 248
-- Data for Name: normas_master_normas; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3402 (class 0 OID 43898)
-- Dependencies: 250
-- Data for Name: normas_subcategories_normas; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (3, '1.1.1 TRANSVERSALES', '2022-02-23 09:41:55.788627-05', '2022-02-23 09:41:55.788642-05', '1011', '2022-02-23 09:44:19.09291-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (4, '1.1.2 VIVIENDA', '2022-02-23 09:42:05.318492-05', '2022-02-23 09:42:05.318508-05', '1012', '2022-02-23 09:44:29.229835-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (1, '1. RNE', '2022-02-23 09:05:01.668184-05', '2022-02-23 09:05:01.6682-05', '10', '2022-02-23 09:45:03.857217-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (6, '2.NORMAS SECTORIALES', '2022-02-23 09:42:40.75365-05', '2022-02-23 09:42:40.753672-05', '20', '2022-02-23 09:45:12.751351-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (10, '3.OPINIONES VINCULANTES', '2022-02-23 09:43:47.504592-05', '2022-02-23 09:43:47.504608-05', '30', '2022-02-23 09:45:20.206555-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (5, '1.2 ESPECIALIDADES RELACIONADAS', '2022-02-23 09:42:26.021685-05', '2022-02-23 09:42:26.021702-05', '102', '2022-02-23 09:45:29.210054-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (7, '2.1 GAS VIVIENDAS ENERGIA Y MINAS', '2022-02-23 09:42:55.086064-05', '2022-02-23 09:42:55.08608-05', '201', '2022-02-23 09:45:51.39454-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (8, '2.2 RATDUS-Ministerio de Vivienda', '2022-02-23 09:43:05.920911-05', '2022-02-23 09:43:05.920929-05', '202', '2022-02-23 09:46:01.573184-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (9, '2.3 VIVIENDA DE INTERES SOCIAL- MIN. DE VIVIENDA', '2022-02-23 09:43:18.567792-05', '2022-02-23 09:43:18.567807-05', '203', '2022-02-23 09:46:12.495256-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (11, '3.1 VIVIENDA DE INTERES SOCIAL- MIN. DE VIVIENDA', '2022-02-23 09:47:30.6806-05', '2022-02-23 09:47:30.680616-05', '301', '2022-02-23 09:47:30.68062-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (12, '4.REGLAMENTO COMENTADO', '2022-02-23 09:47:39.264026-05', '2022-02-23 09:47:39.264041-05', '40', '2022-02-23 09:47:39.264046-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (13, '4.1 NORMA GRAFICA COMENTADA', '2022-02-23 09:47:55.565945-05', '2022-02-23 09:47:55.565961-05', '401', '2022-02-23 09:47:55.565965-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (14, '4.2 CASUISTICA', '2022-02-23 09:48:07.027824-05', '2022-02-23 09:48:07.02784-05', '402', '2022-02-23 09:48:07.027845-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (15, '4.2.1 APELACIONES RECONSIDERACIONES', '2022-02-23 09:48:14.541377-05', '2022-02-23 09:48:14.541393-05', '4021', '2022-02-23 09:48:14.541397-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (16, '4.2.2 CONCLUSIONES DE CHARLAS(OPINION DE ASUNTOS TECNICOS )', '2022-02-23 09:48:29.521568-05', '2022-02-23 09:48:29.521584-05', '4022', '2022-02-23 09:48:29.521589-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (17, '4.2.3 DIRECTIVAS CAP', '2022-02-23 09:48:36.642629-05', '2022-02-23 09:48:36.642645-05', '4023', '2022-02-23 09:48:36.642649-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (18, '5.INDECOPI', '2022-02-23 09:48:48.838397-05', '2022-02-23 09:48:48.838413-05', '50', '2022-02-23 09:48:48.838418-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (19, '6.NORMAS MUNICIPALES', '2022-02-23 09:48:57.13884-05', '2022-02-23 09:48:57.138856-05', '60', '2022-02-23 09:48:57.13886-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (20, '6.1 NORMAS PROVINCIALES', '2022-02-23 09:49:05.241542-05', '2022-02-23 09:49:05.241558-05', '601', '2022-02-23 09:49:05.241563-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (21, '6.2 NORMAS DISTRITALES', '2022-02-23 09:49:11.307929-05', '2022-02-23 09:49:11.307944-05', '602', '2022-02-23 09:49:11.307948-05');
INSERT INTO public.normas_subcategories_normas (id, subcategory_name, register_date_time, created, "order", updated) VALUES (2, '1.1 RNE-ARQUITECTURA', '2022-02-23 09:41:27.328401-05', '2022-02-23 09:41:27.328416-05', '101', '2022-02-23 09:57:31.644659-05');


--
-- TOC entry 3404 (class 0 OID 43903)
-- Dependencies: 252
-- Data for Name: normas_subnormativa; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3406 (class 0 OID 43908)
-- Dependencies: 254
-- Data for Name: register_normativa; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.register_normativa (id, norma, name_denom, base_legal, fecha_publi, tipo_norma_id, tipo_uso_id, document, created, descripcion, es_foro, es_vigente, updated) VALUES (9, 'E.M.070', 'Norma Técnica Transporte Mecánico', 'R.M. N° 084-2019-VIVIENDA', '2019-03-12', 4, 1, NULL, '2022-02-23 16:37:14.087087-05', '', true, true, '2022-02-24 15:00:30.041232-05');
INSERT INTO public.register_normativa (id, norma, name_denom, base_legal, fecha_publi, tipo_norma_id, tipo_uso_id, document, created, descripcion, es_foro, es_vigente, updated) VALUES (10, 'E.M.070', 'FE ERRATAS NT.EM 070', 'FÉ ERRATAS R.M. N° 084-2019-VIVIENDA', '2019-03-24', 4, 1, NULL, '2022-02-23 16:38:07.017105-05', '', true, true, '2022-02-23 16:38:07.017122-05');
INSERT INTO public.register_normativa (id, norma, name_denom, base_legal, fecha_publi, tipo_norma_id, tipo_uso_id, document, created, descripcion, es_foro, es_vigente, updated) VALUES (16, 'REGLAMENTO ESPECIAL  DE HABILITACIÓN URBANA Y EDIFICACIÓN', 'Decreto Supremo que aprueba el Reglamento Especial de Habilitación Urbana y edificiación', 'D.S. Nº 010-2018-VIVIENDA   (DEROGA EL D.S.  Nº 013-2013-VIVIENDA)', '2018-07-11', 3, 1, 'Document_normativa/registros_publicos_consultas_og.pdf', '2022-02-23 17:40:05.180387-05', NULL, true, true, '2022-02-25 16:00:04.787569-05');
INSERT INTO public.register_normativa (id, norma, name_denom, base_legal, fecha_publi, tipo_norma_id, tipo_uso_id, document, created, descripcion, es_foro, es_vigente, updated) VALUES (17, 'GAS GLP', 'Reglam.Seguridad Gas GLP. Art. 122,  4', 'D. S. N° 27-94-EM', '1994-05-17', 6, 1, 'Document_normativa/D.S.027-94-EM_GASLicuadoPetroleo_reglaseguinstalaciones.PDF', '2022-02-23 17:44:02.190901-05', '', true, true, '2022-02-23 17:44:02.190913-05');
INSERT INTO public.register_normativa (id, norma, name_denom, base_legal, fecha_publi, tipo_norma_id, tipo_uso_id, document, created, descripcion, es_foro, es_vigente, updated) VALUES (5, 'G.E.020', 'Componentes y Carácterísticas de las Edificaciones', 'D.S. N° 011-2006-Vivienda', '2006-06-09', 3, 1, 'cbe3b1c4-c7c3-41f0-8aa8-ecc770b96a33.pdf', '2022-02-23 15:20:23.735734-05', '', true, true, '2022-02-23 15:20:23.73575-05');
INSERT INTO public.register_normativa (id, norma, name_denom, base_legal, fecha_publi, tipo_norma_id, tipo_uso_id, document, created, descripcion, es_foro, es_vigente, updated) VALUES (1, 'A.010', 'Condiciones Generales de diseño', 'R.M. N° 191-2021-Vivienda', '2021-07-08', 3, 1, 'Document_normativa/CAP-ManualTecnico-DataLicencias.pdf', '2022-02-23 09:05:56.761188-05', 'una breve descripcion de la norma', true, true, '2022-02-25 16:05:23.921644-05');
INSERT INTO public.register_normativa (id, norma, name_denom, base_legal, fecha_publi, tipo_norma_id, tipo_uso_id, document, created, descripcion, es_foro, es_vigente, updated) VALUES (2, 'A.120', 'Accesibilidad Universal en Edificaciones     ( antes "Accesibilidad para personas con discapacidad")', 'R.M.N° 072-2019 -Vivienda', '2019-03-02', 3, 3, 'Document_normativa/CAP-ManualTecnico-DataLicencias_bAm1jOU.pdf', '2022-02-23 10:03:43.341885-05', NULL, false, false, '2022-02-25 16:05:47.305735-05');
INSERT INTO public.register_normativa (id, norma, name_denom, base_legal, fecha_publi, tipo_norma_id, tipo_uso_id, document, created, descripcion, es_foro, es_vigente, updated) VALUES (18, 'GAS GNV', 'Masificación del Gas Natural ', 'D. S. N° 029-2013-EM', '2013-08-01', 3, 1, 'Document_normativa/D.S._N029-2013-EM_DisposicionesMasificaciónGasNatural_01.08.2013.pdf', '2022-02-23 17:46:20.671172-05', ' incorporación de la "Única Disposición Complementaria"al RNE D.S. N° 011-2006-VIVIENDA, Gas GNV en viviendas.', true, true, '2022-02-23 17:46:20.671192-05');
INSERT INTO public.register_normativa (id, norma, name_denom, base_legal, fecha_publi, tipo_norma_id, tipo_uso_id, document, created, descripcion, es_foro, es_vigente, updated) VALUES (19, 'Opinión Vinculante A', 'Opinion Vinculante', 'ITL_022-2021-VIVIENDA', '2021-03-12', 10, 1, 'Document_normativa/ITL_022-2021-VIVIENDA_Parametros_50PorCientoViviendaVIS_OFICIO_091-_2_ZOoa9DO.pdf', '2022-02-23 18:02:33.907685-05', '', false, true, '2022-02-23 18:02:33.907706-05');
INSERT INTO public.register_normativa (id, norma, name_denom, base_legal, fecha_publi, tipo_norma_id, tipo_uso_id, document, created, descripcion, es_foro, es_vigente, updated) VALUES (6, 'A.020', 'Vivienda', 'D.S. N° 188-2021-Vivienda', '2021-07-07', 3, 3, NULL, '2022-02-23 16:30:05.361645-05', '', true, true, '2022-02-23 16:30:05.361664-05');
INSERT INTO public.register_normativa (id, norma, name_denom, base_legal, fecha_publi, tipo_norma_id, tipo_uso_id, document, created, descripcion, es_foro, es_vigente, updated) VALUES (12, 'GAS GLP', 'Reglam.Seguridad Gas GLP. Art. 122,  4, a) Se permitirán cilindros Tipo 10 déntro de edificios de hasta tres pisos y no más de doce departamentos', 'D. S. N° 27-94-EM', '1994-05-17', 1, 1, 'e2c0fd24-7ed9-40ff-aa9c-0364d588cf1e.pdf', '2022-02-23 16:41:09.394597-05', '', true, true, '2022-02-23 16:41:09.394609-05');
INSERT INTO public.register_normativa (id, norma, name_denom, base_legal, fecha_publi, tipo_norma_id, tipo_uso_id, document, created, descripcion, es_foro, es_vigente, updated) VALUES (4, 'A.130', 'Requisitos de Seguridad  -  Cap. XI : Almacenes y  Cap. XII: Centros de Diversión.', 'D.S. N° 017-2012-Vivienda', '2012-11-09', 3, 3, 'Document_normativa/9addd27b-bc28-4c88-b8c6-c33b4b0a6c07.pdf', '2022-02-23 10:11:04.973077-05', '', false, true, '2022-02-23 10:11:04.973089-05');


--
-- TOC entry 3408 (class 0 OID 43916)
-- Dependencies: 256
-- Data for Name: register_palabclave; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (1, 'ESCALERA', '2022-02-23 09:06:12.563277-05', '2022-02-23 09:06:12.56329-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (2, 'Escaleras Protegidas', '2022-02-23 09:59:28.164551-05', '2022-02-23 09:59:28.164566-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (3, 'Escaleras de Evacuación', '2022-02-23 09:59:40.011091-05', '2022-02-23 09:59:40.011104-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (4, 'Ventilación', '2022-02-23 09:59:51.33371-05', '2022-02-23 09:59:51.333723-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (5, 'Sótanos', '2022-02-23 10:00:24.246462-05', '2022-02-23 10:00:24.246476-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (6, 'Retiros', '2022-02-23 10:00:24.2568-05', '2022-02-23 10:00:24.256813-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (7, 'Altura de edificación', '2022-02-23 10:00:24.265838-05', '2022-02-23 10:00:24.265851-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (8, 'Proyectos', '2022-02-23 15:22:24.664564-05', '2022-02-23 15:22:24.664582-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (9, 'características', '2022-02-23 15:22:24.692652-05', '2022-02-23 15:22:24.69267-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (10, 'Anteproyecto', '2022-02-23 15:22:24.704593-05', '2022-02-23 15:22:24.704613-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (11, 'Especialidades', '2022-02-23 15:22:24.716517-05', '2022-02-23 15:22:24.716535-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (12, 'A.010', '2022-02-23 16:31:18.450421-05', '2022-02-23 16:31:18.450435-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (13, 'A.020', '2022-02-23 16:49:23.436572-05', '2022-02-23 16:49:23.436591-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (14, 'Edificacion Residencial', '2022-02-23 16:49:23.449456-05', '2022-02-23 16:49:23.449475-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (15, 'Definicion', '2022-02-23 16:49:23.459277-05', '2022-02-23 16:49:23.459297-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (16, 'Tipologías', '2022-02-23 16:49:23.468992-05', '2022-02-23 16:49:23.469029-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (17, 'Grupos familiares', '2022-02-23 16:49:23.477856-05', '2022-02-23 16:49:23.477869-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (18, 'Transporte mecanico', '2022-02-23 16:50:34.542881-05', '2022-02-23 16:50:34.5429-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (19, 'ascensores', '2022-02-23 16:50:34.563789-05', '2022-02-23 16:50:34.563808-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (20, 'Especificaciones tecnicas', '2022-02-23 16:50:34.57847-05', '2022-02-23 16:50:34.578488-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (21, 'Diseño', '2022-02-23 16:50:34.588766-05', '2022-02-23 16:50:34.588784-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (22, 'Instalación', '2022-02-23 16:50:34.598447-05', '2022-02-23 16:50:34.598465-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (23, 'Montacargas', '2022-02-23 16:50:34.607863-05', '2022-02-23 16:50:34.607881-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (24, 'EM.070', '2022-02-23 16:51:30.01247-05', '2022-02-23 16:51:30.012488-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (25, 'D. S. N° 27-94-EM', '2022-02-23 16:54:01.140114-05', '2022-02-23 16:54:01.140129-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (26, 'Cilindros Tipo 10', '2022-02-23 16:54:01.15014-05', '2022-02-23 16:54:01.150158-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (27, 'Edificios de hasta 3 pisos', '2022-02-23 16:54:01.157747-05', '2022-02-23 16:54:01.15776-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (28, 'Cilindros Tipo 10 prohibido en sótanos', '2022-02-23 16:54:01.165014-05', '2022-02-23 16:54:01.165027-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (29, 'Cilindros Tipo 10 prohibidos en Cajas de Escaleras', '2022-02-23 16:54:01.172503-05', '2022-02-23 16:54:01.172516-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (30, 'D. S. N° 029-2013-EM', '2022-02-23 16:54:39.854859-05', '2022-02-23 16:54:39.854872-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (31, 'Suministro domiciliario', '2022-02-23 16:54:39.865342-05', '2022-02-23 16:54:39.865355-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (32, 'GNV', '2022-02-23 16:54:39.873587-05', '2022-02-23 16:54:39.873599-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (33, 'Edificaciones Multifamiliares', '2022-02-23 16:54:39.881408-05', '2022-02-23 16:54:39.881421-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (34, 'D.S. Nº 022-2016-VIVIENDA Acondicionamiento Territorial', '2022-02-23 16:56:02.979954-05', '2022-02-23 16:56:02.979973-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (35, 'Actividad económica', '2022-02-23 16:56:02.996073-05', '2022-02-23 16:56:02.996091-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (38, 'Estructura urbana', '2022-02-23 16:56:03.023956-05', '2022-02-23 16:56:03.023968-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (39, 'Reglamento especial', '2022-02-23 17:41:34.182588-05', '2022-02-23 17:41:34.182609-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (40, 'D.S. Nº 010-2018-VIVIENDA', '2022-02-23 17:41:34.193817-05', '2022-02-23 17:41:34.193835-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (41, 'habilitacion urbana', '2022-02-23 17:41:34.211539-05', '2022-02-23 17:41:34.211554-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (42, 'Buscador', '2022-02-23 17:46:07.329057-05', '2022-02-23 17:46:07.329077-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (43, 'Puerta', '2022-02-23 17:46:07.345868-05', '2022-02-23 17:46:07.345886-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (44, 'Escaleras en Comercio', '2022-02-23 17:47:04.100403-05', '2022-02-23 17:47:04.100425-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (45, 'restaurantes', '2022-02-23 18:07:44.792516-05', '2022-02-23 18:07:44.792539-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (46, 'ESPECIALIDADES RELACIONADAS', '2022-02-23 18:48:50.080031-05', '2022-02-23 18:48:50.080045-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (36, 'Centro Poblado', '2022-02-23 16:56:03.008449-05', '2022-02-24 23:20:41.766155-05');
INSERT INTO public.register_palabclave (id, name, created, updated) VALUES (37, 'Edificación', '2022-02-23 16:56:03.016527-05', '2022-02-24 23:27:29.601822-05');


--
-- TOC entry 3410 (class 0 OID 43921)
-- Dependencies: 258
-- Data for Name: register_palabclave_normativas; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (2, 1, 1);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (3, 2, 1);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (4, 3, 1);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (5, 4, 1);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (6, 5, 1);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (7, 6, 1);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (8, 7, 1);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (9, 8, 5);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (10, 9, 5);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (11, 10, 5);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (12, 11, 5);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (13, 12, 1);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (14, 13, 6);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (15, 14, 6);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (16, 15, 6);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (17, 16, 6);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (18, 17, 6);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (19, 18, 9);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (20, 19, 9);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (21, 20, 9);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (22, 21, 9);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (23, 22, 9);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (24, 23, 9);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (25, 18, 10);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (26, 19, 10);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (27, 20, 10);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (28, 21, 10);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (29, 22, 10);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (30, 23, 10);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (31, 24, 10);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (37, 24, 9);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (45, 25, 12);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (46, 26, 12);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (47, 27, 12);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (48, 28, 12);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (49, 29, 12);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (59, 39, 16);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (60, 40, 16);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (61, 41, 16);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (62, 42, 4);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (63, 43, 4);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (64, 3, 4);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (67, 4, 18);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (69, 30, 18);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (70, 31, 18);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (71, 32, 18);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (72, 33, 18);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (74, 45, 1);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (76, 36, 17);
INSERT INTO public.register_palabclave_normativas (id, register_palabraclave_id, register_normativa_id) VALUES (77, 37, 6);


--
-- TOC entry 3447 (class 0 OID 0)
-- Dependencies: 201
-- Name: apps_control_payment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.apps_control_payment_id_seq', 1, false);


--
-- TOC entry 3448 (class 0 OID 0)
-- Dependencies: 203
-- Name: apps_member_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.apps_member_id_seq', 3, true);


--
-- TOC entry 3449 (class 0 OID 0)
-- Dependencies: 205
-- Name: apps_plan_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.apps_plan_id_seq', 1, false);


--
-- TOC entry 3450 (class 0 OID 0)
-- Dependencies: 207
-- Name: apps_policies_usage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.apps_policies_usage_id_seq', 1, false);


--
-- TOC entry 3451 (class 0 OID 0)
-- Dependencies: 209
-- Name: apps_policies_usage_norma_name_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.apps_policies_usage_norma_name_id_seq', 1, false);


--
-- TOC entry 3452 (class 0 OID 0)
-- Dependencies: 212
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 3, true);


--
-- TOC entry 3453 (class 0 OID 0)
-- Dependencies: 214
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 96, true);


--
-- TOC entry 3454 (class 0 OID 0)
-- Dependencies: 216
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 96, true);


--
-- TOC entry 3455 (class 0 OID 0)
-- Dependencies: 219
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 4, true);


--
-- TOC entry 3456 (class 0 OID 0)
-- Dependencies: 220
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 4, true);


--
-- TOC entry 3457 (class 0 OID 0)
-- Dependencies: 222
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 3458 (class 0 OID 0)
-- Dependencies: 224
-- Name: bus_normativa_date_normativa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bus_normativa_date_normativa_id_seq', 1, false);


--
-- TOC entry 3459 (class 0 OID 0)
-- Dependencies: 226
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 51, true);


--
-- TOC entry 3460 (class 0 OID 0)
-- Dependencies: 228
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 24, true);


--
-- TOC entry 3461 (class 0 OID 0)
-- Dependencies: 230
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 26, true);


--
-- TOC entry 3462 (class 0 OID 0)
-- Dependencies: 233
-- Name: foro_categories_foro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.foro_categories_foro_id_seq', 1, false);


--
-- TOC entry 3463 (class 0 OID 0)
-- Dependencies: 235
-- Name: foro_coments_foro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.foro_coments_foro_id_seq', 1, true);


--
-- TOC entry 3464 (class 0 OID 0)
-- Dependencies: 237
-- Name: foro_subcategories_foro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.foro_subcategories_foro_id_seq', 1, false);


--
-- TOC entry 3465 (class 0 OID 0)
-- Dependencies: 239
-- Name: foro_themas_foro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.foro_themas_foro_id_seq', 1, false);


--
-- TOC entry 3466 (class 0 OID 0)
-- Dependencies: 241
-- Name: normas_areas_normas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.normas_areas_normas_id_seq', 3, true);


--
-- TOC entry 3467 (class 0 OID 0)
-- Dependencies: 244
-- Name: normas_categories_normas_area_name_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.normas_categories_normas_area_name_id_seq', 1, false);


--
-- TOC entry 3468 (class 0 OID 0)
-- Dependencies: 245
-- Name: normas_categories_normas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.normas_categories_normas_id_seq', 1, false);


--
-- TOC entry 3469 (class 0 OID 0)
-- Dependencies: 247
-- Name: normas_location_normas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.normas_location_normas_id_seq', 1, false);


--
-- TOC entry 3470 (class 0 OID 0)
-- Dependencies: 249
-- Name: normas_master_normas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.normas_master_normas_id_seq', 1, false);


--
-- TOC entry 3471 (class 0 OID 0)
-- Dependencies: 251
-- Name: normas_subcategories_normas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.normas_subcategories_normas_id_seq', 21, true);


--
-- TOC entry 3472 (class 0 OID 0)
-- Dependencies: 253
-- Name: normas_subnormativa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.normas_subnormativa_id_seq', 1, false);


--
-- TOC entry 3473 (class 0 OID 0)
-- Dependencies: 255
-- Name: register_normativa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.register_normativa_id_seq', 19, true);


--
-- TOC entry 3474 (class 0 OID 0)
-- Dependencies: 257
-- Name: register_palabclave_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.register_palabclave_id_seq', 46, true);


--
-- TOC entry 3475 (class 0 OID 0)
-- Dependencies: 259
-- Name: register_palabclave_normativas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.register_palabclave_normativas_id_seq', 79, true);


--
-- TOC entry 3070 (class 2606 OID 43956)
-- Name: apps_control_payment apps_control_payment_id_plan_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_control_payment
    ADD CONSTRAINT apps_control_payment_id_plan_id_key UNIQUE (id_plan_id);


--
-- TOC entry 3072 (class 2606 OID 43958)
-- Name: apps_control_payment apps_control_payment_member_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_control_payment
    ADD CONSTRAINT apps_control_payment_member_id_key UNIQUE (member_id);


--
-- TOC entry 3074 (class 2606 OID 43960)
-- Name: apps_control_payment apps_control_payment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_control_payment
    ADD CONSTRAINT apps_control_payment_pkey PRIMARY KEY (id);


--
-- TOC entry 3076 (class 2606 OID 43962)
-- Name: apps_member apps_member_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_member
    ADD CONSTRAINT apps_member_pkey PRIMARY KEY (id);


--
-- TOC entry 3078 (class 2606 OID 43964)
-- Name: apps_member apps_member_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_member
    ADD CONSTRAINT apps_member_user_id_key UNIQUE (user_id);


--
-- TOC entry 3080 (class 2606 OID 43966)
-- Name: apps_plan apps_plan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_plan
    ADD CONSTRAINT apps_plan_pkey PRIMARY KEY (id);


--
-- TOC entry 3084 (class 2606 OID 43968)
-- Name: apps_policies_usage_norma_name apps_policies_usage_norm_policies_usage_id_master_df38f46a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_policies_usage_norma_name
    ADD CONSTRAINT apps_policies_usage_norm_policies_usage_id_master_df38f46a_uniq UNIQUE (policies_usage_id, master_normas_id);


--
-- TOC entry 3087 (class 2606 OID 43970)
-- Name: apps_policies_usage_norma_name apps_policies_usage_norma_name_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_policies_usage_norma_name
    ADD CONSTRAINT apps_policies_usage_norma_name_pkey PRIMARY KEY (id);


--
-- TOC entry 3082 (class 2606 OID 43972)
-- Name: apps_policies_usage apps_policies_usage_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_policies_usage
    ADD CONSTRAINT apps_policies_usage_pkey PRIMARY KEY (id);


--
-- TOC entry 3090 (class 2606 OID 43974)
-- Name: apps_usertoken apps_usertoken_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_usertoken
    ADD CONSTRAINT apps_usertoken_pkey PRIMARY KEY (token);


--
-- TOC entry 3092 (class 2606 OID 43976)
-- Name: apps_usertoken apps_usertoken_user_profile_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_usertoken
    ADD CONSTRAINT apps_usertoken_user_profile_id_key UNIQUE (user_profile_id);


--
-- TOC entry 3095 (class 2606 OID 43978)
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 3100 (class 2606 OID 43980)
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- TOC entry 3103 (class 2606 OID 43982)
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3097 (class 2606 OID 43984)
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 3106 (class 2606 OID 43986)
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- TOC entry 3108 (class 2606 OID 43988)
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 3116 (class 2606 OID 43990)
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 3119 (class 2606 OID 43992)
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- TOC entry 3110 (class 2606 OID 43994)
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- TOC entry 3122 (class 2606 OID 43996)
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3125 (class 2606 OID 43998)
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- TOC entry 3113 (class 2606 OID 44000)
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- TOC entry 3127 (class 2606 OID 44002)
-- Name: busqueda_normativa bus_normativa_date_normativa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.busqueda_normativa
    ADD CONSTRAINT bus_normativa_date_normativa_pkey PRIMARY KEY (id);


--
-- TOC entry 3130 (class 2606 OID 44004)
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 3133 (class 2606 OID 44006)
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- TOC entry 3135 (class 2606 OID 44008)
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 3137 (class 2606 OID 44010)
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 3140 (class 2606 OID 44012)
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 3143 (class 2606 OID 44014)
-- Name: foro_categories_foro foro_categories_foro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foro_categories_foro
    ADD CONSTRAINT foro_categories_foro_pkey PRIMARY KEY (id);


--
-- TOC entry 3145 (class 2606 OID 44016)
-- Name: foro_coments_foro foro_coments_foro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foro_coments_foro
    ADD CONSTRAINT foro_coments_foro_pkey PRIMARY KEY (id);


--
-- TOC entry 3150 (class 2606 OID 44018)
-- Name: foro_subcategories_foro foro_subcategories_foro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foro_subcategories_foro
    ADD CONSTRAINT foro_subcategories_foro_pkey PRIMARY KEY (id);


--
-- TOC entry 3152 (class 2606 OID 44020)
-- Name: foro_themas_foro foro_themas_foro_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foro_themas_foro
    ADD CONSTRAINT foro_themas_foro_pkey PRIMARY KEY (id);


--
-- TOC entry 3155 (class 2606 OID 44022)
-- Name: normas_areas_normas normas_areas_normas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_areas_normas
    ADD CONSTRAINT normas_areas_normas_pkey PRIMARY KEY (id);


--
-- TOC entry 3161 (class 2606 OID 44024)
-- Name: normas_categories_normas_area_name normas_categories_normas_area_name_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_categories_normas_area_name
    ADD CONSTRAINT normas_categories_normas_area_name_pkey PRIMARY KEY (id);


--
-- TOC entry 3163 (class 2606 OID 44026)
-- Name: normas_categories_normas_area_name normas_categories_normas_categories_normas_id_are_47ddaf98_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_categories_normas_area_name
    ADD CONSTRAINT normas_categories_normas_categories_normas_id_are_47ddaf98_uniq UNIQUE (categories_normas_id, areas_normas_id);


--
-- TOC entry 3157 (class 2606 OID 44028)
-- Name: normas_categories_normas normas_categories_normas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_categories_normas
    ADD CONSTRAINT normas_categories_normas_pkey PRIMARY KEY (id);


--
-- TOC entry 3165 (class 2606 OID 44030)
-- Name: normas_location_normas normas_location_normas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_location_normas
    ADD CONSTRAINT normas_location_normas_pkey PRIMARY KEY (id);


--
-- TOC entry 3170 (class 2606 OID 44032)
-- Name: normas_master_normas normas_master_normas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_master_normas
    ADD CONSTRAINT normas_master_normas_pkey PRIMARY KEY (id);


--
-- TOC entry 3173 (class 2606 OID 44034)
-- Name: normas_subcategories_normas normas_subcategories_normas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_subcategories_normas
    ADD CONSTRAINT normas_subcategories_normas_pkey PRIMARY KEY (id);


--
-- TOC entry 3176 (class 2606 OID 44036)
-- Name: normas_subnormativa normas_subnormativa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_subnormativa
    ADD CONSTRAINT normas_subnormativa_pkey PRIMARY KEY (id);


--
-- TOC entry 3178 (class 2606 OID 44038)
-- Name: register_normativa register_normativa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.register_normativa
    ADD CONSTRAINT register_normativa_pkey PRIMARY KEY (id);


--
-- TOC entry 3183 (class 2606 OID 44040)
-- Name: register_palabclave register_palabclave_name_04850c43_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.register_palabclave
    ADD CONSTRAINT register_palabclave_name_04850c43_uniq UNIQUE (name);


--
-- TOC entry 3187 (class 2606 OID 44042)
-- Name: register_palabclave_normativas register_palabclave_norm_register_palabraclave_id_9d85626b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.register_palabclave_normativas
    ADD CONSTRAINT register_palabclave_norm_register_palabraclave_id_9d85626b_uniq UNIQUE (register_palabraclave_id, register_normativa_id);


--
-- TOC entry 3190 (class 2606 OID 44044)
-- Name: register_palabclave_normativas register_palabclave_normativas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.register_palabclave_normativas
    ADD CONSTRAINT register_palabclave_normativas_pkey PRIMARY KEY (id);


--
-- TOC entry 3185 (class 2606 OID 44046)
-- Name: register_palabclave register_palabclave_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.register_palabclave
    ADD CONSTRAINT register_palabclave_pkey PRIMARY KEY (id);


--
-- TOC entry 3085 (class 1259 OID 44047)
-- Name: apps_policies_usage_norma_name_master_normas_id_ce05d1c1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX apps_policies_usage_norma_name_master_normas_id_ce05d1c1 ON public.apps_policies_usage_norma_name USING btree (master_normas_id);


--
-- TOC entry 3088 (class 1259 OID 44048)
-- Name: apps_policies_usage_norma_name_policies_usage_id_12215f98; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX apps_policies_usage_norma_name_policies_usage_id_12215f98 ON public.apps_policies_usage_norma_name USING btree (policies_usage_id);


--
-- TOC entry 3093 (class 1259 OID 44049)
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 3098 (class 1259 OID 44050)
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- TOC entry 3101 (class 1259 OID 44051)
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- TOC entry 3104 (class 1259 OID 44052)
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- TOC entry 3114 (class 1259 OID 44053)
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- TOC entry 3117 (class 1259 OID 44054)
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- TOC entry 3120 (class 1259 OID 44055)
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- TOC entry 3123 (class 1259 OID 44056)
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- TOC entry 3111 (class 1259 OID 44057)
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- TOC entry 3128 (class 1259 OID 44058)
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- TOC entry 3131 (class 1259 OID 44059)
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- TOC entry 3138 (class 1259 OID 44060)
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- TOC entry 3141 (class 1259 OID 44061)
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 3146 (class 1259 OID 44062)
-- Name: foro_coments_foro_tema_id_11260671; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX foro_coments_foro_tema_id_11260671 ON public.foro_coments_foro USING btree (tema_id);


--
-- TOC entry 3147 (class 1259 OID 44063)
-- Name: foro_coments_foro_user_id_78cffa1f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX foro_coments_foro_user_id_78cffa1f ON public.foro_coments_foro USING btree (user_id);


--
-- TOC entry 3148 (class 1259 OID 44064)
-- Name: foro_subcategories_foro_categories_id_f9ce4436; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX foro_subcategories_foro_categories_id_f9ce4436 ON public.foro_subcategories_foro USING btree (categories_id);


--
-- TOC entry 3153 (class 1259 OID 44065)
-- Name: foro_themas_foro_subcategories_id_a9000b0b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX foro_themas_foro_subcategories_id_a9000b0b ON public.foro_themas_foro USING btree (subcategories_id);


--
-- TOC entry 3158 (class 1259 OID 44066)
-- Name: normas_categories_normas_a_categories_normas_id_b3912345; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX normas_categories_normas_a_categories_normas_id_b3912345 ON public.normas_categories_normas_area_name USING btree (categories_normas_id);


--
-- TOC entry 3159 (class 1259 OID 44067)
-- Name: normas_categories_normas_area_name_areas_normas_id_14011aa9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX normas_categories_normas_area_name_areas_normas_id_14011aa9 ON public.normas_categories_normas_area_name USING btree (areas_normas_id);


--
-- TOC entry 3166 (class 1259 OID 44068)
-- Name: normas_master_normas_area_name_id_65d15a7d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX normas_master_normas_area_name_id_65d15a7d ON public.normas_master_normas USING btree (area_name_id);


--
-- TOC entry 3167 (class 1259 OID 44069)
-- Name: normas_master_normas_category_name_id_345c5df2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX normas_master_normas_category_name_id_345c5df2 ON public.normas_master_normas USING btree (category_name_id);


--
-- TOC entry 3168 (class 1259 OID 44070)
-- Name: normas_master_normas_location_name_id_5bfae735; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX normas_master_normas_location_name_id_5bfae735 ON public.normas_master_normas USING btree (location_name_id);


--
-- TOC entry 3171 (class 1259 OID 44071)
-- Name: normas_master_normas_subcategory_name_id_0eef7552; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX normas_master_normas_subcategory_name_id_0eef7552 ON public.normas_master_normas USING btree (subcategory_name_id);


--
-- TOC entry 3174 (class 1259 OID 44072)
-- Name: normas_subnormativa_norma_sub_id_452170b5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX normas_subnormativa_norma_sub_id_452170b5 ON public.normas_subnormativa USING btree (norma_sub_id);


--
-- TOC entry 3179 (class 1259 OID 44073)
-- Name: register_normativa_tipo_norma_id_a959a74f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX register_normativa_tipo_norma_id_a959a74f ON public.register_normativa USING btree (tipo_norma_id);


--
-- TOC entry 3180 (class 1259 OID 44074)
-- Name: register_normativa_tipo_uso_id_f247ddb2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX register_normativa_tipo_uso_id_f247ddb2 ON public.register_normativa USING btree (tipo_uso_id);


--
-- TOC entry 3181 (class 1259 OID 44075)
-- Name: register_palabclave_name_04850c43_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX register_palabclave_name_04850c43_like ON public.register_palabclave USING btree (name varchar_pattern_ops);


--
-- TOC entry 3188 (class 1259 OID 44076)
-- Name: register_palabclave_normat_register_palabraclave_id_306db7d7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX register_palabclave_normat_register_palabraclave_id_306db7d7 ON public.register_palabclave_normativas USING btree (register_palabraclave_id);


--
-- TOC entry 3191 (class 1259 OID 44077)
-- Name: register_palabclave_normativas_register_normativa_id_18a9f3cb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX register_palabclave_normativas_register_normativa_id_18a9f3cb ON public.register_palabclave_normativas USING btree (register_normativa_id);


--
-- TOC entry 3192 (class 2606 OID 44078)
-- Name: apps_control_payment apps_control_payment_id_plan_id_dd8631b5_fk_apps_plan_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_control_payment
    ADD CONSTRAINT apps_control_payment_id_plan_id_dd8631b5_fk_apps_plan_id FOREIGN KEY (id_plan_id) REFERENCES public.apps_plan(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3193 (class 2606 OID 44083)
-- Name: apps_control_payment apps_control_payment_member_id_f58a04ed_fk_apps_member_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_control_payment
    ADD CONSTRAINT apps_control_payment_member_id_f58a04ed_fk_apps_member_id FOREIGN KEY (member_id) REFERENCES public.apps_member(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3194 (class 2606 OID 44088)
-- Name: apps_member apps_member_user_id_76200006_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_member
    ADD CONSTRAINT apps_member_user_id_76200006_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3195 (class 2606 OID 44093)
-- Name: apps_policies_usage_norma_name apps_policies_usage__master_normas_id_ce05d1c1_fk_normas_ma; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_policies_usage_norma_name
    ADD CONSTRAINT apps_policies_usage__master_normas_id_ce05d1c1_fk_normas_ma FOREIGN KEY (master_normas_id) REFERENCES public.normas_master_normas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3196 (class 2606 OID 44098)
-- Name: apps_policies_usage_norma_name apps_policies_usage__policies_usage_id_12215f98_fk_apps_poli; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_policies_usage_norma_name
    ADD CONSTRAINT apps_policies_usage__policies_usage_id_12215f98_fk_apps_poli FOREIGN KEY (policies_usage_id) REFERENCES public.apps_policies_usage(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3197 (class 2606 OID 44103)
-- Name: apps_usertoken apps_usertoken_user_profile_id_6cb5ce36_fk_apps_member_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apps_usertoken
    ADD CONSTRAINT apps_usertoken_user_profile_id_6cb5ce36_fk_apps_member_id FOREIGN KEY (user_profile_id) REFERENCES public.apps_member(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3198 (class 2606 OID 44108)
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3199 (class 2606 OID 44113)
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3200 (class 2606 OID 44118)
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3201 (class 2606 OID 44123)
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3202 (class 2606 OID 44128)
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3203 (class 2606 OID 44133)
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3204 (class 2606 OID 44138)
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3205 (class 2606 OID 44143)
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3206 (class 2606 OID 44148)
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3207 (class 2606 OID 44153)
-- Name: foro_coments_foro foro_coments_foro_tema_id_11260671_fk_register_normativa_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foro_coments_foro
    ADD CONSTRAINT foro_coments_foro_tema_id_11260671_fk_register_normativa_id FOREIGN KEY (tema_id) REFERENCES public.register_normativa(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3208 (class 2606 OID 44158)
-- Name: foro_coments_foro foro_coments_foro_user_id_78cffa1f_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foro_coments_foro
    ADD CONSTRAINT foro_coments_foro_user_id_78cffa1f_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3209 (class 2606 OID 44163)
-- Name: foro_subcategories_foro foro_subcategories_f_categories_id_f9ce4436_fk_foro_cate; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foro_subcategories_foro
    ADD CONSTRAINT foro_subcategories_f_categories_id_f9ce4436_fk_foro_cate FOREIGN KEY (categories_id) REFERENCES public.foro_categories_foro(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3210 (class 2606 OID 44168)
-- Name: foro_themas_foro foro_themas_foro_subcategories_id_a9000b0b_fk_foro_subc; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.foro_themas_foro
    ADD CONSTRAINT foro_themas_foro_subcategories_id_a9000b0b_fk_foro_subc FOREIGN KEY (subcategories_id) REFERENCES public.foro_subcategories_foro(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3211 (class 2606 OID 44173)
-- Name: normas_categories_normas_area_name normas_categories_no_areas_normas_id_14011aa9_fk_normas_ar; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_categories_normas_area_name
    ADD CONSTRAINT normas_categories_no_areas_normas_id_14011aa9_fk_normas_ar FOREIGN KEY (areas_normas_id) REFERENCES public.normas_areas_normas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3212 (class 2606 OID 44178)
-- Name: normas_categories_normas_area_name normas_categories_no_categories_normas_id_b3912345_fk_normas_ca; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_categories_normas_area_name
    ADD CONSTRAINT normas_categories_no_categories_normas_id_b3912345_fk_normas_ca FOREIGN KEY (categories_normas_id) REFERENCES public.normas_categories_normas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3213 (class 2606 OID 44183)
-- Name: normas_master_normas normas_master_normas_area_name_id_65d15a7d_fk_normas_ar; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_master_normas
    ADD CONSTRAINT normas_master_normas_area_name_id_65d15a7d_fk_normas_ar FOREIGN KEY (area_name_id) REFERENCES public.normas_areas_normas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3214 (class 2606 OID 44188)
-- Name: normas_master_normas normas_master_normas_category_name_id_345c5df2_fk_normas_ca; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_master_normas
    ADD CONSTRAINT normas_master_normas_category_name_id_345c5df2_fk_normas_ca FOREIGN KEY (category_name_id) REFERENCES public.normas_categories_normas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3215 (class 2606 OID 44193)
-- Name: normas_master_normas normas_master_normas_location_name_id_5bfae735_fk_normas_lo; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_master_normas
    ADD CONSTRAINT normas_master_normas_location_name_id_5bfae735_fk_normas_lo FOREIGN KEY (location_name_id) REFERENCES public.normas_location_normas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3216 (class 2606 OID 44198)
-- Name: normas_master_normas normas_master_normas_subcategory_name_id_0eef7552_fk_normas_su; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_master_normas
    ADD CONSTRAINT normas_master_normas_subcategory_name_id_0eef7552_fk_normas_su FOREIGN KEY (subcategory_name_id) REFERENCES public.normas_subcategories_normas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3217 (class 2606 OID 44203)
-- Name: normas_subnormativa normas_subnormativa_norma_sub_id_452170b5_fk_normas_su; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.normas_subnormativa
    ADD CONSTRAINT normas_subnormativa_norma_sub_id_452170b5_fk_normas_su FOREIGN KEY (norma_sub_id) REFERENCES public.normas_subcategories_normas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3218 (class 2606 OID 44208)
-- Name: register_normativa register_normativa_tipo_norma_id_a959a74f_fk_normas_su; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.register_normativa
    ADD CONSTRAINT register_normativa_tipo_norma_id_a959a74f_fk_normas_su FOREIGN KEY (tipo_norma_id) REFERENCES public.normas_subcategories_normas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3219 (class 2606 OID 44213)
-- Name: register_normativa register_normativa_tipo_uso_id_f247ddb2_fk_normas_ar; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.register_normativa
    ADD CONSTRAINT register_normativa_tipo_uso_id_f247ddb2_fk_normas_ar FOREIGN KEY (tipo_uso_id) REFERENCES public.normas_areas_normas(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3220 (class 2606 OID 44218)
-- Name: register_palabclave_normativas register_palabclave__register_normativa_i_18a9f3cb_fk_register_; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.register_palabclave_normativas
    ADD CONSTRAINT register_palabclave__register_normativa_i_18a9f3cb_fk_register_ FOREIGN KEY (register_normativa_id) REFERENCES public.register_normativa(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 3221 (class 2606 OID 44223)
-- Name: register_palabclave_normativas register_palabclave__register_palabraclav_306db7d7_fk_register_; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.register_palabclave_normativas
    ADD CONSTRAINT register_palabclave__register_palabraclav_306db7d7_fk_register_ FOREIGN KEY (register_palabraclave_id) REFERENCES public.register_palabclave(id) DEFERRABLE INITIALLY DEFERRED;


-- Completed on 2022-02-28 12:26:32

--
-- PostgreSQL database dump complete
--

