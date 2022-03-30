--
-- PostgreSQL database dump
--

-- Dumped from database version 13.5
-- Dumped by pg_dump version 13.5

-- Started on 2022-03-02 15:48:13

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

--
-- TOC entry 3363 (class 0 OID 44279)
-- Dependencies: 211
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (2, 'pbkdf2_sha256$260000$nQxFFQgzpSKYqKOh3yR5OX$KLUYDJQvW8xkG/FA6sD7qy69HYTrXqKvb5x7RnegSIc=', '2022-02-23 15:06:37.249871-05', false, '789', '', 'VILLEGAS', 'avillegas@dt-data.com', false, true, '2022-02-23 15:04:58.162346-05');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (4, 'pbkdf2_sha256$260000$fABGEJ4YT9gflkg69ZoSAO$mUiVTFhBZ4eMvZfHF1jyUOh5LDoApIsFNyVxCvH2dM8=', '2022-02-23 16:56:32.136343-05', false, '2000', '', 'user1', 'suyon.jesus@gmail.com', false, true, '2022-02-23 16:56:14.929374-05');
INSERT INTO public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1, 'pbkdf2_sha256$260000$XRGIXI5BUrrutsxPbrxfBw$GNEUDNOXDwqRMMqhveAugEaBFR2RgKfKpRyOpe+URQM=', '2022-03-02 12:46:57.85332-05', true, 'jaime', 'Jaime', 'Marston', 'jaime@gmail.com', true, true, '2022-02-23 09:01:30-05');


--
-- TOC entry 3391 (class 0 OID 44601)
-- Dependencies: 239
-- Data for Name: apps_member; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.apps_member (id, first_surname, second_surname, names, full_name, person_type, identity, profession, mobile, phone, email, tuition, secret_code, address, area_interest, institution, photo, register_date_time, user_id) VALUES (1, 'VILLEGAS', 'PACHECO', 'ANDREA GIULIANA', 'Nombre completo', 'N', '73684340', 'A', '935863306', '017809960', 'avillegas@dt-data.com', 789, 1234, 'av.san jose 123', '', '', '', '2022-02-23 15:04:58.134334-05', NULL);
INSERT INTO public.apps_member (id, first_surname, second_surname, names, full_name, person_type, identity, profession, mobile, phone, email, tuition, secret_code, address, area_interest, institution, photo, register_date_time, user_id) VALUES (3, 'user1', 'user1', 'user1', 'Nombre completo', 'N', '83928194', 'A', '923678387', '333333', 'suyon.jesus@gmail.com', 2000, 22, 'k3jmkm', '', '', '', '2022-02-23 16:56:14.923323-05', NULL);


--
-- TOC entry 3393 (class 0 OID 44616)
-- Dependencies: 241
-- Data for Name: apps_plan; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3398 (class 0 OID 44650)
-- Dependencies: 246
-- Data for Name: apps_control_payment; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3396 (class 0 OID 44631)
-- Dependencies: 244
-- Data for Name: apps_policies_usage; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.apps_policies_usage (id, title, message, validity_date_start, validity_date_finish, register_date_time) VALUES (1, 'Deserunt', 'Fuga Laborum Qui m  quis ut quam aut sunt dolor omnis voluptatum dicta sed qui est ut culpa reiciendis eu quis et  quis ut quam aut sunt dolor omnis voluptatum dicta sed qui est ut culpa reiciendis eu quis et  quis ut quam aut sunt dolor omnis voluptatum dicta sed qui est ut culpa reiciendis eu quis et', '2022-03-01', '2022-03-25', '2022-03-02 08:36:37.388873-05');
INSERT INTO public.apps_policies_usage (id, title, message, validity_date_start, validity_date_finish, register_date_time) VALUES (2, 'Dolor', 'Quaerat ullamco cill sint aspernatur sed est mollitia culpa sint Qui m quis ut quam aut sunt dolor omnis voluptatum dicta sed qui est ut culpa reiciendis eu quis et quis ut quam aut sunt dolor omnis voluptatum dicta sed qui est ut culpa reiciendis eu quis et quis ut quam aut sunt dolor omnis voluptatum dicta sed qui est ut culpa reiciendis eu quis et
Norma Ref:', '2021-05-19', '2022-06-17', '2022-03-02 08:37:52.245367-05');


--
-- TOC entry 3371 (class 0 OID 44381)
-- Dependencies: 219
-- Data for Name: normas_areas_normas; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.normas_areas_normas (id, name, register_date_time, created, updated) VALUES (1, 'VIVIENDA', '2022-02-23 09:04:41.996554-05', '2022-02-23 09:04:41.996568-05', '2022-02-23 09:04:41.996572-05');
INSERT INTO public.normas_areas_normas (id, name, register_date_time, created, updated) VALUES (3, 'RESTAURANTES', '2022-02-23 18:03:24.311788-05', '2022-02-23 18:03:24.311808-05', '2022-02-23 18:03:24.311815-05');


--
-- TOC entry 3381 (class 0 OID 44424)
-- Dependencies: 229
-- Data for Name: normas_subcategories_normas; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (3, '1.1.1 TRANSVERSALES', '2022-02-23 09:41:55.788627-05', '2022-02-23 09:41:55.788642-05', '1011', '2022-02-23 09:44:19.09291-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (4, '1.1.2 VIVIENDA', '2022-02-23 09:42:05.318492-05', '2022-02-23 09:42:05.318508-05', '1012', '2022-02-23 09:44:29.229835-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (1, '1. RNE', '2022-02-23 09:05:01.668184-05', '2022-02-23 09:05:01.6682-05', '10', '2022-02-23 09:45:03.857217-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (6, '2.NORMAS SECTORIALES', '2022-02-23 09:42:40.75365-05', '2022-02-23 09:42:40.753672-05', '20', '2022-02-23 09:45:12.751351-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (10, '3.OPINIONES VINCULANTES', '2022-02-23 09:43:47.504592-05', '2022-02-23 09:43:47.504608-05', '30', '2022-02-23 09:45:20.206555-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (5, '1.2 ESPECIALIDADES RELACIONADAS', '2022-02-23 09:42:26.021685-05', '2022-02-23 09:42:26.021702-05', '102', '2022-02-23 09:45:29.210054-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (7, '2.1 GAS VIVIENDAS ENERGIA Y MINAS', '2022-02-23 09:42:55.086064-05', '2022-02-23 09:42:55.08608-05', '201', '2022-02-23 09:45:51.39454-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (8, '2.2 RATDUS-Ministerio de Vivienda', '2022-02-23 09:43:05.920911-05', '2022-02-23 09:43:05.920929-05', '202', '2022-02-23 09:46:01.573184-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (9, '2.3 VIVIENDA DE INTERES SOCIAL- MIN. DE VIVIENDA', '2022-02-23 09:43:18.567792-05', '2022-02-23 09:43:18.567807-05', '203', '2022-02-23 09:46:12.495256-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (11, '3.1 VIVIENDA DE INTERES SOCIAL- MIN. DE VIVIENDA', '2022-02-23 09:47:30.6806-05', '2022-02-23 09:47:30.680616-05', '301', '2022-02-23 09:47:30.68062-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (12, '4.REGLAMENTO COMENTADO', '2022-02-23 09:47:39.264026-05', '2022-02-23 09:47:39.264041-05', '40', '2022-02-23 09:47:39.264046-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (13, '4.1 NORMA GRAFICA COMENTADA', '2022-02-23 09:47:55.565945-05', '2022-02-23 09:47:55.565961-05', '401', '2022-02-23 09:47:55.565965-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (14, '4.2 CASUISTICA', '2022-02-23 09:48:07.027824-05', '2022-02-23 09:48:07.02784-05', '402', '2022-02-23 09:48:07.027845-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (15, '4.2.1 APELACIONES RECONSIDERACIONES', '2022-02-23 09:48:14.541377-05', '2022-02-23 09:48:14.541393-05', '4021', '2022-02-23 09:48:14.541397-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (16, '4.2.2 CONCLUSIONES DE CHARLAS(OPINION DE ASUNTOS TECNICOS )', '2022-02-23 09:48:29.521568-05', '2022-02-23 09:48:29.521584-05', '4022', '2022-02-23 09:48:29.521589-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (17, '4.2.3 DIRECTIVAS CAP', '2022-02-23 09:48:36.642629-05', '2022-02-23 09:48:36.642645-05', '4023', '2022-02-23 09:48:36.642649-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (18, '5.INDECOPI', '2022-02-23 09:48:48.838397-05', '2022-02-23 09:48:48.838413-05', '50', '2022-02-23 09:48:48.838418-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (19, '6.NORMAS MUNICIPALES', '2022-02-23 09:48:57.13884-05', '2022-02-23 09:48:57.138856-05', '60', '2022-02-23 09:48:57.13886-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (20, '6.1 NORMAS PROVINCIALES', '2022-02-23 09:49:05.241542-05', '2022-02-23 09:49:05.241558-05', '601', '2022-02-23 09:49:05.241563-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (21, '6.2 NORMAS DISTRITALES', '2022-02-23 09:49:11.307929-05', '2022-02-23 09:49:11.307944-05', '602', '2022-02-23 09:49:11.307948-05');
INSERT INTO public.normas_subcategories_normas (id, name, register_date_time, created, "order", updated) VALUES (2, '1.1 RNE-ARQUITECTURA', '2022-02-23 09:41:27.328401-05', '2022-02-23 09:41:27.328416-05', '101', '2022-02-23 09:57:31.644659-05');


--
-- TOC entry 3379 (class 0 OID 44413)
-- Dependencies: 227
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
-- TOC entry 3400 (class 0 OID 44696)
-- Dependencies: 248
-- Data for Name: apps_policies_usage_norma; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.apps_policies_usage_norma (id, policies_usage_id, register_normativa_id) VALUES (1, 1, 1);
INSERT INTO public.apps_policies_usage_norma (id, policies_usage_id, register_normativa_id) VALUES (2, 1, 2);
INSERT INTO public.apps_policies_usage_norma (id, policies_usage_id, register_normativa_id) VALUES (3, 1, 6);
INSERT INTO public.apps_policies_usage_norma (id, policies_usage_id, register_normativa_id) VALUES (4, 2, 1);
INSERT INTO public.apps_policies_usage_norma (id, policies_usage_id, register_normativa_id) VALUES (5, 2, 10);
INSERT INTO public.apps_policies_usage_norma (id, policies_usage_id, register_normativa_id) VALUES (6, 2, 12);
INSERT INTO public.apps_policies_usage_norma (id, policies_usage_id, register_normativa_id) VALUES (7, 2, 18);
INSERT INTO public.apps_policies_usage_norma (id, policies_usage_id, register_normativa_id) VALUES (8, 2, 19);


--
-- TOC entry 3394 (class 0 OID 44622)
-- Dependencies: 242
-- Data for Name: apps_usertoken; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3359 (class 0 OID 44261)
-- Dependencies: 207
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_group (id, name) VALUES (1, 'Premium');
INSERT INTO public.auth_group (id, name) VALUES (2, 'Profesional');
INSERT INTO public.auth_group (id, name) VALUES (3, 'Gratuito');


--
-- TOC entry 3355 (class 0 OID 44243)
-- Dependencies: 203
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
-- TOC entry 3357 (class 0 OID 44253)
-- Dependencies: 205
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
-- TOC entry 3361 (class 0 OID 44271)
-- Dependencies: 209
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3365 (class 0 OID 44289)
-- Dependencies: 213
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (1, 1, 1);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (2, 2, 3);
INSERT INTO public.auth_user_groups (id, user_id, group_id) VALUES (4, 4, 3);


--
-- TOC entry 3367 (class 0 OID 44297)
-- Dependencies: 215
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3402 (class 0 OID 44727)
-- Dependencies: 250
-- Data for Name: busqueda_normativa; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3369 (class 0 OID 44357)
-- Dependencies: 217
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (1, '2022-03-02 08:36:37.398873-05', '1', 'Policies_usage object (1)', 1, '[{"added": {}}]', 10, 1);
INSERT INTO public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (2, '2022-03-02 08:37:52.253369-05', '2', 'Policies_usage object (2)', 1, '[{"added": {}}]', 10, 1);


--
-- TOC entry 3353 (class 0 OID 44232)
-- Dependencies: 201
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_migrations (id, app, name, applied) VALUES (1, 'contenttypes', '0001_initial', '2022-03-02 08:29:16.206524-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (2, 'auth', '0001_initial', '2022-03-02 08:29:17.11304-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (3, 'admin', '0001_initial', '2022-03-02 08:29:17.257679-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2022-03-02 08:29:17.273066-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2022-03-02 08:29:17.284081-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (6, 'normas', '0001_initial', '2022-03-02 08:29:17.944229-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (7, 'normas', '0002_auto_20220302_0823', '2022-03-02 08:29:18.740931-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (8, 'apps', '0001_initial', '2022-03-02 08:29:19.158612-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (9, 'apps', '0002_auto_20220302_0823', '2022-03-02 08:29:19.324854-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (10, 'contenttypes', '0002_remove_content_type_name', '2022-03-02 08:29:19.370478-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (11, 'auth', '0002_alter_permission_name_max_length', '2022-03-02 08:29:19.386479-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (12, 'auth', '0003_alter_user_email_max_length', '2022-03-02 08:29:19.403479-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (13, 'auth', '0004_alter_user_username_opts', '2022-03-02 08:29:19.415479-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (14, 'auth', '0005_alter_user_last_login_null', '2022-03-02 08:29:19.43148-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (15, 'auth', '0006_require_contenttypes_0002', '2022-03-02 08:29:19.435482-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (16, 'auth', '0007_alter_validators_add_error_messages', '2022-03-02 08:29:19.453482-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (17, 'auth', '0008_alter_user_username_max_length', '2022-03-02 08:29:19.509935-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (18, 'auth', '0009_alter_user_last_name_max_length', '2022-03-02 08:29:19.525925-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (19, 'auth', '0010_alter_group_name_max_length', '2022-03-02 08:29:19.546361-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (20, 'auth', '0011_update_proxy_permissions', '2022-03-02 08:29:19.574364-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (21, 'auth', '0012_alter_user_first_name_max_length', '2022-03-02 08:29:19.588353-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (22, 'bus_normativa', '0001_initial', '2022-03-02 08:29:19.640408-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (23, 'bus_normativa', '0002_alter_date_normativa_table', '2022-03-02 08:29:19.648426-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (24, 'foro', '0001_initial', '2022-03-02 08:29:19.914898-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (25, 'foro', '0002_auto_20220302_0823', '2022-03-02 08:29:20.025234-05');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (26, 'sessions', '0001_initial', '2022-03-02 08:29:20.125354-05');


--
-- TOC entry 3411 (class 0 OID 44795)
-- Dependencies: 259
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('3xxabr3wgo0e075j28t8pifpizu5cyni', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nPP8F:vAvracFauP2pL5qmy89iTkXdr0Lrn6Sqn_9TOWaBFHU', '2022-03-16 08:35:07.914448-05');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('fqk2xktzjamqc8orx3p0fjspxyq83c82', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nPP8z:_5ymtBgQMxCrS4xVpXRjoyLDqgYsX-0Fk3WARx_529c', '2022-03-16 08:35:53.984861-05');
INSERT INTO public.django_session (session_key, session_data, expire_date) VALUES ('148dp2ovbp2626pum58p6zoxga1rqclx', '.eJxVjEEOwiAQRe_C2pABBiQu3XsGMsAgVQNJaVfGu9smXej2vff_WwRalxrWwXOYsrgIJU6_LFJ6cttFflC7d5l6W-Ypyj2Rhx3y1jO_rkf7d1Bp1G1NwFCUQqXR85kSmuLZFkQAB856yNaYkoyziY2LceMIZHXUroBTRXy-w7Q27A:1nPT3x:RRpKCOvpamF772_Ob7lCmbNUCD5OZjVARS1Hq3MqlPM', '2022-03-16 12:46:57.861295-05');


--
-- TOC entry 3404 (class 0 OID 44738)
-- Dependencies: 252
-- Data for Name: foro_categories_foro; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3410 (class 0 OID 44762)
-- Dependencies: 258
-- Data for Name: foro_coments_foro; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.foro_coments_foro (id, coments, likes, dislikes, register_date_time, user_id, tema_id) VALUES (1, 'un comentario', 0, 0, '2022-02-23 09:06:48.524386-05', 1, 1);


--
-- TOC entry 3406 (class 0 OID 44746)
-- Dependencies: 254
-- Data for Name: foro_subcategories_foro; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3408 (class 0 OID 44754)
-- Dependencies: 256
-- Data for Name: foro_themas_foro; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3373 (class 0 OID 44389)
-- Dependencies: 221
-- Data for Name: normas_categories_normas; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3375 (class 0 OID 44397)
-- Dependencies: 223
-- Data for Name: normas_categories_normas_name; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3377 (class 0 OID 44405)
-- Dependencies: 225
-- Data for Name: normas_location_normas; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3387 (class 0 OID 44451)
-- Dependencies: 235
-- Data for Name: normas_master_normas; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3383 (class 0 OID 44432)
-- Dependencies: 231
-- Data for Name: normas_subnormativa; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3385 (class 0 OID 44440)
-- Dependencies: 233
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
-- TOC entry 3389 (class 0 OID 44525)
-- Dependencies: 237
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
-- TOC entry 3417 (class 0 OID 0)
-- Dependencies: 245
-- Name: apps_control_payment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.apps_control_payment_id_seq', 1, false);


--
-- TOC entry 3418 (class 0 OID 0)
-- Dependencies: 238
-- Name: apps_member_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.apps_member_id_seq', 1, false);


--
-- TOC entry 3419 (class 0 OID 0)
-- Dependencies: 240
-- Name: apps_plan_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.apps_plan_id_seq', 1, false);


--
-- TOC entry 3420 (class 0 OID 0)
-- Dependencies: 243
-- Name: apps_policies_usage_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.apps_policies_usage_id_seq', 2, true);


--
-- TOC entry 3421 (class 0 OID 0)
-- Dependencies: 247
-- Name: apps_policies_usage_norma_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.apps_policies_usage_norma_id_seq', 8, true);


--
-- TOC entry 3422 (class 0 OID 0)
-- Dependencies: 206
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- TOC entry 3423 (class 0 OID 0)
-- Dependencies: 208
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 3424 (class 0 OID 0)
-- Dependencies: 204
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 96, true);


--
-- TOC entry 3425 (class 0 OID 0)
-- Dependencies: 212
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- TOC entry 3426 (class 0 OID 0)
-- Dependencies: 210
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- TOC entry 3427 (class 0 OID 0)
-- Dependencies: 214
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 3428 (class 0 OID 0)
-- Dependencies: 249
-- Name: bus_normativa_date_normativa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bus_normativa_date_normativa_id_seq', 1, false);


--
-- TOC entry 3429 (class 0 OID 0)
-- Dependencies: 216
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 2, true);


--
-- TOC entry 3430 (class 0 OID 0)
-- Dependencies: 202
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 24, true);


--
-- TOC entry 3431 (class 0 OID 0)
-- Dependencies: 200
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 26, true);


--
-- TOC entry 3432 (class 0 OID 0)
-- Dependencies: 251
-- Name: foro_categories_foro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.foro_categories_foro_id_seq', 1, false);


--
-- TOC entry 3433 (class 0 OID 0)
-- Dependencies: 257
-- Name: foro_coments_foro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.foro_coments_foro_id_seq', 1, false);


--
-- TOC entry 3434 (class 0 OID 0)
-- Dependencies: 253
-- Name: foro_subcategories_foro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.foro_subcategories_foro_id_seq', 1, false);


--
-- TOC entry 3435 (class 0 OID 0)
-- Dependencies: 255
-- Name: foro_themas_foro_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.foro_themas_foro_id_seq', 1, false);


--
-- TOC entry 3436 (class 0 OID 0)
-- Dependencies: 218
-- Name: normas_areas_normas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.normas_areas_normas_id_seq', 1, false);


--
-- TOC entry 3437 (class 0 OID 0)
-- Dependencies: 222
-- Name: normas_categories_normas_name_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.normas_categories_normas_name_id_seq', 1, false);


--
-- TOC entry 3438 (class 0 OID 0)
-- Dependencies: 220
-- Name: normas_categories_normas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.normas_categories_normas_id_seq', 1, false);


--
-- TOC entry 3439 (class 0 OID 0)
-- Dependencies: 224
-- Name: normas_location_normas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.normas_location_normas_id_seq', 1, false);


--
-- TOC entry 3440 (class 0 OID 0)
-- Dependencies: 234
-- Name: normas_master_normas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.normas_master_normas_id_seq', 1, false);


--
-- TOC entry 3441 (class 0 OID 0)
-- Dependencies: 228
-- Name: normas_subcategories_normas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.normas_subcategories_normas_id_seq', 1, false);


--
-- TOC entry 3442 (class 0 OID 0)
-- Dependencies: 230
-- Name: normas_subnormativa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.normas_subnormativa_id_seq', 1, false);


--
-- TOC entry 3443 (class 0 OID 0)
-- Dependencies: 226
-- Name: register_normativa_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.register_normativa_id_seq', 1, false);


--
-- TOC entry 3444 (class 0 OID 0)
-- Dependencies: 232
-- Name: register_palabclave_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.register_palabclave_id_seq', 1, false);


--
-- TOC entry 3445 (class 0 OID 0)
-- Dependencies: 236
-- Name: register_palabclave_normativas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.register_palabclave_normativas_id_seq', 1, false);


-- Completed on 2022-03-02 15:48:15

--
-- PostgreSQL database dump complete
--

