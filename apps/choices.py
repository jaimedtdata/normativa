
METODPAY_CHOICES= (
    ('E', 'VISA'),
    ('V', 'EFECTIVO'),
)

PROFESSION_CHOICES = (
    ('A', 'ARQUITECTO'),
    ('I', 'INGENIERO'),
)

PLATAFORMA_TYPE_CHOICES = (
    ('F', 'FORO'),
    ('N', 'NORMAS'),
)

PERSON_TYPE_CHOICES = (
    ('N', 'NATURAL'),
    ('J', 'JURÍDICA'),
)

USER_ROLES = (
	('1', 'Gratuito'),
	('2', 'Premium'),
	('3', 'Profesional'),
)

ADHOC_INSTITUTION_CHOICES = (
	('','---------'),
	('MC','MINISTERIO DE CULTURA'),
	('SE','SERNANP'),
)

SPECIALTY_CHOICES = (
	('','---------'),
	('SA','SALUD'),
	('SCI','SEGURIDAD CONTRA INCENDIOS'),
	('VI','VIAL'),
	('O','OTROS'),
)

AREAS_CHOICES = (
	'Legal',
	'Ventas',
	'Atención al Cliente',
	'Corporativo',
	'Desarrollos',
)

SPECIALTIES_CHOICES = (
	'Arquitectura',
	'Ingeniería',
	'Contabilidad',
	'Finanzas',
	'Gerencia',
	'Derecho',
)

PUESTOS_CHOICES = (
	'Full Time',
	'Part Time',
	'Prácticas Pre Profesionales',
)

works_list = (
	{
		'title': 'Asesor Comercial',
		'area': 'Corporativo',
		'location': 'Miraflores',
		'icon': 'fa fa-building',
		'fecha': 'Hoy',
	},
	{
		'title': 'Abogado',
		'area': 'Legal',
		'location': 'Cercado de Lima',
		'icon': 'fa fa-suitcase',
		'fecha': 'Ayer',
	},
	{
		'title': 'Arquitecto',
		'area': 'Desarrollo',
		'location': 'Santiago de Surco',
		'icon': 'fa fa-city',
		'fecha': 'Ayer',
	},
	{
		'title': 'Analista de Inteligencia de Negocios',
		'area': 'Finanzas',
		'location': 'San Isidro',
		'icon': 'fa fa-dollar-sign',
		'fecha': '25/11/2020',
	},
	{
		'title': 'Contador',
		'area': 'Contabilidad',
		'location': 'San Isidro',
		'icon': 'fa fa-dollar-sign',
		'fecha': '25/11/2020',
	},
	{
		'title': 'Gerente de Filial',
		'area': 'Corporativo',
		'location': 'Miraflores',
		'icon': 'fa fa-building',
		'fecha': '24/11/2020',
	},

)
RULES_CATEGORIES = (
	('Normas Legales'),
	('Ley Orgánica'),
	('Últimas Normas SMV'),
	('Resolución'),
	('Directivas'),
	('Consulta Ciudadana'),
	('Consulta Ciudadana Histórica'),
	('Ley de Transparencia'),
	('Criterios de Sanción'),
)

SANCTIONS_CATEGORIES = (
	('Sanciones Último Trimestre'),
	('Sanciones por Supervisado'),
	('Por Tipo Empresa'),
)

PREVENTIONS_CHOICES = (
	('Política y Plan Nacional'),
	('Recomendaciones'),
	('Regulación General'),
	('Regulación Sectorial del Mercado de Valores'),
)

# SECTIONS_CHOICES = (
# 	('','-------- Todos --------'),
# 	('','RNE'),
# 	('','Ley de Procedimientos 29090 -  Ley General 27444'),
# 	('','Normas Sectoriales'),
# 	('','Normas Tecnicas'),
# 	('','Normas Distritales'),
# 	('','Cartas Pronunciamente - Opiniones Vinculantes'),
# 	('','Ordenanzas'),
# )


RULES_TYPES = (
	('','-------- Todos --------'),
	('','Hospedaje'),
	('','Educación'),
	('','Salud'),
)


LOCATIONS_CHOICES = (
	('','-------- Todos --------'),
	('','MML'),
	('','Nacional'),
)


DENOMS = (
	'Reporte de Sostenibilidad Corporativa',
	'Modificación de párrafos de Secciones VI, VII, IX; y numeral 5 del anexo I del modelo de presencial de la entidad valorizadora responsable de determinar el precio mínimo a ser tomado en cuenta en los procesos de ofertas públicas de compra por exclusión y ofertas públicas de adquisición”',
	'Modificar artículos de Reglamentos de Agentes de Intermediación, Fondos Mutuos de inversión en Valores, Fondos de Inversión y sus Sociedades Administradoras, Empresas Proveedoras de Precios, Normas para la Prevención del Lavado de Activos y Financiamiento del Terrorismo',
	'Nuevo Reglamento del Sistema MVNet y SMV Virtual',
	'Aprobar el modelo de “Bases para el proceso de selección no presencial de la entidad valorizadora responsable de determinar el precio mínimo a ser tomado en cuenta en los procesos de ofertas públicas de compra por exclusión y ofertas públicas de adquisición',
	'Norma Sobre Contribuciones Por Los Servicios De Supervisión Que Presta Conasev',
	'Modificar la Primera Disposición Transitoria del Reglamento del Mercado Alternativo de Valores – MAV, aprobado por Resolución SMV N° 025-2012-SMV/01,',
	'Artículo Modificado Del Estatuto De Cavali S.a. Iclv',
	'Reglamento Del Mercado Alternativo De Valores - Mav / Manual Para El Cumplimiento De Los Requisitos Aplicables A Las Ofertas Públicas De Instrumentos De Corto Plazo Emitidos Por Empresas En El Mav',
	'Nuevo plazo para la presentación de información financiera y otras anual del ejercicio 2019 y 2020',
	'Modificación Del Artículo Cuadragésimo Noveno A Del Estatuto Social De La Bolsa De Valores De Lima S.a.a.	',
	'Estatuto Social De La Bolsa De Valores De Lima',
	'Nuevos Plazos Para La Entrega De Determinada Información',
	'Modificar Los Artículos 58, 61, 62, 63, 64, 65 Y 71 Del Reglamento De Operaciones En Rueda De Bolsa De La Bolsa De Valores De Lima',
	'Reglamento De Operaciones En Rueda De Bolsa',
	'Aprueban El Reglamento De Instituciones De Compensación Y Liquidación De Valores A Que Se Refiere El Título Viii De La Ley Del Mercado De Valores',
	'Modifica Articulos Del Reglamento De Instituciones De Compensación Y Liquidación De Valores',
	'Modificar El Primer Párrafo Del Artículo 17 Del Reglamento General Del Curso De Especialización En Mercado De Valores',
	'Aprueban Las «normas Para Las Convocatorias Y Celebraciones De Juntas Generales De Accionistas Y Asambleas De Obligacionistas No Presenciales A Que Se Refiere El Artículo 5 Del Decreto De Urgencia N° 056-2020',
	'Disposiciones aplicables a la Corporación Financiera de Desarrollo S.A. – COFIDE, para actuar como sociedad titulizadora, en el marco de los Programas y Fondos creados por el Estado Peruano para la reactivación económica del país',
)

import random

def get_rules():
	rules = []
	# for i in range(1, random.randint(3,100)):
	# 	SECTION = random.choice(SECTIONS_CHOICES)[1]
	# 	RULE_TYPE = random.choice(RULES_TYPES)[1]
	# 	LOCATIONS = random.choice(LOCATIONS_CHOICES)[1]
	# 	rules.append(
	# 		{
	# 			'n': i,
	# 			'section': SECTIONS_CHOICES[1][1] if SECTION == SECTIONS_CHOICES[0][1] else SECTION,
	# 			'rule_type': RULES_TYPES[1][1] if RULE_TYPE == RULES_TYPES[0][1] else RULE_TYPE,
	# 			'locations': LOCATIONS_CHOICES[1][1] if LOCATIONS == LOCATIONS_CHOICES[0][1] else LOCATIONS,
	# 			'norm': 'RSUP 000{} - 2020'.format(random.randint(1,100)),
	# 			'denom': random.choice(DENOMS),
	# 			'publication_date': '{}/{}/{}'.format(random.randint(1,31),random.randint(1,12),random.randint(2000,2020))
	# 		}
	# 	)
	return rules

def get_foro_items():
    	
	
	category_list = (
		{
			'title': 'Temas Normativos',
			'items': [
				{
					'title':'Licencias, Procedimientos Administrativos  para Licencias de Edificación',
					'themes_count': random.randint(10,50),
					'messages_count': random.randint(50,200),
					'last_messages': (
						{
							'message':'Arq. Mayra Rojas',
							'date':'Hoy {}:{} {}'.format(random.randint(1,12), random.randint(10,59), random.choice(['a.m.','p.m.'])),						
						},
						{
							'message':'Arq. Juan Villanueva',		
							'date':'Ayer {}:{} {}'.format(random.randint(1,12), random.randint(10,59), random.choice(['a.m.','p.m.'])),						
						},
					)
				},
				{
					'title':'Convenios',
					'themes_count': random.randint(10,50),
					'messages_count': random.randint(50,200),
					'last_messages': (
						{
							'message':'Convenio Rimac Seguros',
							'date':'Hoy {}:{} {}'.format(random.randint(1,12), random.randint(10,59), random.choice(['a.m.','p.m.'])),						
						},
						{
							'message':'Convenio Clínica Ricardo Palma',
							'date':'Ayer {}:{} {}'.format(random.randint(1,12), random.randint(10,59), random.choice(['a.m.','p.m.'])),						
						},
					)
				},				
			],
		},
		
	)
	return category_list

def get_themes():
	users = (
		('ariel12',False),
		('max2020',True),
		('superarquitecto',True),
		('megaarquitecto',False),
		('maria2021',False),
		('juan_12',True),
		('jorge_3',True),
		('jaime23',True),
	)
	themes = []
	for x in range(1,15):
		themes.append(
			{
				'theme': random.choice(random.choice(random.choice(get_foro_items())['items'])['last_messages'])['message'],
				'user': random.choice(users),
				'date':'Hoy {}:{} {}'.format(random.randint(1,12), random.randint(10,59), random.choice(['a.m.','p.m.'])),						
			},
		)
	return themes

def get_coments():
	themes = []
	for x in range(1,15):
		themes.append(
			{
				'theme': '',
				'user': '',
				'comment': '',
				'date':'Hoy {}:{} {}'.format(random.randint(1,12), random.randint(10,59), random.choice(['a.m.','p.m.'])),						
			},
		)
	return themes