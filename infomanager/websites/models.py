from django.db import models

class Site(models.model):
    '''
    Representa un sitio web o aplicación
    '''
    nombre = models.CharField(unique=True, verbose_name=u'Nombre', max_length=100)
    dominio = models.CharField(unique=True, verbose_name=u'Dominio', max_length=100)
    url_home= models.CharField(unique=True, verbose_name=u'Url', max_length=200)
    descripcion = models.CharField(verbose_name=u'Descripción', max_length=1000)
    unidad = models.CharField(verbose_name=u'Unidad responsable', max_length=100)
    contacto = models.CharField(verbose_name=u'Contacto', max_length=200)
    resp_tecnico = models.CharField(verbose_name=u'Responsable técnico', max_length=200)
    resp_actualizacion = models.CharField(verbose_name=u'Responsable actualización', max_length=200)
    fecha_creacion = models.DateTimeField(verbose_name=u'Fecha creación')
    fecha_actualizacion = models.DateTimeField(verbose_name=u'Fecha actualización')
    emp_desarrolladora = models.ForeignKey(ServiceProvider, verbose_name=u'Empresa desarrolladora', max_length=200)
    emp_mantenimiento =models.ForeignKey(ServiceProvider, verbose_name=u'Empresa mantenimiento', max_length=200)
    fecha_fin_contrato = models.DateTimeField(verbose_name=u'Fecha fin del contrato')
    tamagno = models.IntegerField( verbose_name=u'Tamaño (#páginas)')
    visitas = models.IntegerField( verbose_name=u'Visitas')
    analytics = models.CharField(verbose_name=u'Analytics', max_length=100)
    autenticacion =models.BooleanField(default=True, verbose_name=u'Tiene autenticación')
    tipo = models.ForeignKey(SiteType, verbose_name=u'Tipo de sitio', blank=True, null=True)
    tipo_contenido = models.ForeignKey(ContentType, verbose_name=u'Tipo de contenido', blank=True, null=True)
    estado = models.ForeignKey(State, verbose_name=u'Estado', blank=True, null=True)
    categoria = models.ForeignKey(Category, verbose_name=u'Categoría', blank=True, null=True)
    ##IMAGEN
    #SERVICIOS INTERNOS INTEGRADOS, SERVICIOS EXTERNOS INTEGRADOS
    servicios = models.ManyToManyField(Service, blank=True, null=True)
    ubicacion = models.ForeignKey(Location, verbose_name=u'Ubicación sitio desplegado', blank=True, null=True)
    tecnologias = models.ManyToManyField(Technology, blank=True, null=True)
    disegno = models.CharField(verbose_name=u'Diseño', max_length=1000)
    #AUDICIENCIAS
    #tickets
    #observacion

    def natural_key(self):
        return dict(dominio=self.dominio, nombre=self.nombre, url=self.url_home)

    class Meta:
        verbose_name = u'Sitio'
        verbose_name_plural = u'Sitios'
        unique_together = ('nombre', 'dominio', 'url_home')

    def __unicode__(self):
        return self.nombre + '_' + self.dominio

class SiteType(models.model):
    type = models.CharField(unique=True, verbose_name=u'Tipo', max_length=100)

    def natural_key(self):
        return dict(type=self.type)

    class Meta:
        verbose_name = u'Tipo de sitio'
        verbose_name_plural = u'Tipos de sitio'

    def __unicode__(self):
        return self.type

class ContentType(models.model):
    type = models.CharField(unique=True, verbose_name=u'Tipo', max_length=100)

    def natural_key(self):
        return dict(type=self.type)

    class Meta:
        verbose_name = u'Tipo de contenido'
        verbose_name_plural = u'Tipos de contenidos'

    def __unicode__(self):
        return self.type

class State(models.model):
    state = models.CharField(unique=True, verbose_name=u'Estado', max_length=100)

    def natural_key(self):
        return dict(state=self.state)

    class Meta:
        verbose_name = u'Estado'
        verbose_name_plural = u'Estados'

    def __unicode__(self):
        return self.state

class Category(models.model):
    category = models.CharField(unique=True, verbose_name=u'Categoría', max_length=100)

    def natural_key(self):
        return dict(category=self.category)

    class Meta:
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

    def __unicode__(self):
        return self.category

class Service(models.model):
    nombre = models.CharField(verbose_name=u'Nombre del servicio', max_length=100)
    descripcion = models.CharField(verbose_name=u'Descripción', max_length=1000)
    proveedor = models.ForeignKey(ServiceProvider, verbose_name=u'Proveedor', blank=True, null=True)
    es_externo =models.BooleanField(default=False, verbose_name=u'Es externo')
    sitios = models.ManyToManyField(Site, blank=True, null=True)

    def natural_key(self):
        return dict(nombre=self.nombre, proveedor=self.proveedor.nombre)

    class Meta:
        verbose_name = u'Servicio Integrado'
        verbose_name_plural = u'Servicios Integrados'


class ServiceProvider(models.model):
    nombre = models.CharField(unique=True, verbose_name=u'Nombre del proveedor', max_length=100)
    descripcion = models.CharField(verbose_name=u'Descripción del proveedor', max_length=1000)

    def natural_key(self):
        return dict(nombre=self.nombre)

    class Meta:
        verbose_name = u'Proveedor'
        verbose_name_plural = u'Proveedores'

    def __unicode__(self):
        return self.nombre

class Location(models.model):
    direccion = models.CharField(verbose_name=u'Dirección', max_length=100)
    proveedor = models.ForeignKey(ServiceProvider, verbose_name=u'Proveedor', blank=True, null=True)

    def natural_key(self):
        return dict(nombre=self.direccion, proveedor=self.proveedor.nombre)

    class Meta:
        verbose_name = u'Ubicación'
        verbose_name_plural = u'Ubicaciones'

    def __unicode__(self):
        return self.direccion

class Technology(models.model)
    nombre = models.CharField(verbose_name=u'Nombre', max_length=100)
    version = models.CharField(verbose_name=u'Versión', max_length=100)

    def natural_key(self):
        return dict(nombre=self.nombre, version=self.version)

    class Meta:
        verbose_name = u'Tecnología'
        verbose_name_plural = u'Tecnologías'

    def __unicode__(self):
        return self.nombre + '_' + self.version
