from django.db import models


class ServiceProvider(models.Model):
    '''
    Representa la compañia o departamento que brinda el servicio
    '''
    name = models.CharField(unique=True, verbose_name=u'Nombre del proveedor', max_length=100)
    description = models.CharField(verbose_name=u'Descripción del proveedor', max_length=1000)

    def natural_key(self):
        return dict(name=self.name)

    class Meta:
        verbose_name = u'Proveedor'
        verbose_name_plural = u'Proveedores'

    def __unicode__(self):
        return self.name
class SiteType(models.Model):
    '''
    Representa el tipo de sitio web o aplicación. Ejemplo: Sitio, Aplicación, Cotenido dinámico
    '''
    type = models.CharField(unique=True, verbose_name=u'Tipo', max_length=100)

    def natural_key(self):
        return dict(type=self.type)

    class Meta:
        verbose_name = u'Tipo de sitio'
        verbose_name_plural = u'Tipos de sitio'

    def __unicode__(self):
        return self.type

class ContentType(models.Model):
    '''
    Representa el tipo de contenido de los sitios. Ejemplo: contenido estático, contenido dinámico
    '''
    type = models.CharField(unique=True, verbose_name=u'Tipo', max_length=100)

    def natural_key(self):
        return dict(type=self.type)

    class Meta:
        verbose_name = u'Tipo de contenido'
        verbose_name_plural = u'Tipos de contenidos'

    def __unicode__(self):
        return self.type

class State(models.Model):
    '''
    Representa el estado que puede tener un sitio. Ejemplo: Activo, actualizado, abandonado
    '''
    state = models.CharField(unique=True, verbose_name=u'Estado', max_length=100)

    def natural_key(self):
        return dict(state=self.state)

    class Meta:
        verbose_name = u'Estado'
        verbose_name_plural = u'Estados'

    def __unicode__(self):
        return self.state

class Category(models.Model):
    '''
    Representa la categoría de los sitios. Ejemplo: Proyecto, Evento, Unidad académica
    '''
    category = models.CharField(unique=True, verbose_name=u'Categoría', max_length=100)

    def natural_key(self):
        return dict(category=self.category)

    class Meta:
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

    def __unicode__(self):
        return self.category

class Service(models.Model):
    '''
    Representa los servicios de los que hace uso la aplicación, ya sean internos como integración con banner, o externos como servicios en la nube.
    '''
    name = models.CharField(verbose_name=u'Nombre del servicio', max_length=100)
    description = models.CharField(verbose_name=u'Descripción', max_length=1000)
    provider = models.ForeignKey(ServiceProvider, verbose_name=u'Proveedor', blank=True, null=True, on_delete=models.DO_NOTHING)
    es_externo =models.BooleanField(default=False, verbose_name=u'Es externo')

    def natural_key(self):
        return dict(name=self.name, provider=self.provider.name)

    class Meta:
        verbose_name = u'Servicio Integrado'
        verbose_name_plural = u'Servicios Integrados'



class Location(models.Model):
    '''
    Ubicación donde se encuentra el sitio desplegado
    '''
    location = models.CharField(verbose_name=u'Ubicación del sitio', max_length=100)
    provider = models.ForeignKey(ServiceProvider, verbose_name=u'Proveedor', blank=True, null=True, on_delete=models.DO_NOTHING)

    def natural_key(self):
        return dict(location=self.location, provider=self.provider.name)

    class Meta:
        verbose_name = u'Ubicación'
        verbose_name_plural = u'Ubicaciones'

    def __unicode__(self):
        return self.location

class TechnologyType(models.Model):
    '''
    Tipos de tecnologías usadas en los sitios. Ejemplo: framework web, plugin, SEO
    '''
    type = models.CharField(verbose_name=u'Type', max_length=100)

    def natural_key(self):
        return dict(type=self.type)

    class Meta:
        verbose_name = u'Tipo de tecnología'
        verbose_name_plural = u'Tipos de tecnologías'

    def __unicode__(self):
        return self.type

class Technology(models.Model):
    '''
    Tecnologías que son usadas por los sitios
    '''
    name = models.CharField(verbose_name=u'Nombre', max_length=100)
    version = models.CharField(verbose_name=u'Versión', max_length=100)
    type = models.ForeignKey(TechnologyType, verbose_name=u'Tipo de tecnología', blank=True, null=True, on_delete=models.DO_NOTHING)

    def natural_key(self):
        return dict(name=self.name, version=self.version)

    class Meta:
        verbose_name = u'Tecnología'
        verbose_name_plural = u'Tecnologías'

    def __unicode__(self):
        return self.name + '_' + self.version


class Audience(models.Model):
    '''
    Audiencias de los sitios. Ejemplo: estudiantes, graduados, público en general
    '''
    name = models.CharField(verbose_name=u'Nombre', max_length=100)

    def natural_key(self):
        return dict(name=self.name)

    class Meta:
        verbose_name = u'Audiencia'
        verbose_name_plural = u'Audiencias'

    def __unicode__(self):
        return self.name


class Site(models.Model):
    '''
    Representa un sitio web o aplicación
    '''
    name = models.CharField(unique=True, verbose_name=u'Nombre', max_length=100)
    domain = models.CharField(unique=True, verbose_name=u'Dominio', max_length=100)
    url_home= models.CharField(unique=True, verbose_name=u'Url', max_length=200)
    description = models.CharField(verbose_name=u'Descripción', max_length=1000)
    unit = models.CharField(verbose_name=u'Unidad responsable', max_length=100)
    contact = models.CharField(verbose_name=u'Contacto', max_length=200)
    tech_resp = models.CharField(verbose_name=u'Responsable técnico', max_length=200)
    update_resp = models.CharField(verbose_name=u'Responsable actualización', max_length=200)
    creation_date = models.DateTimeField(verbose_name=u'Fecha creación')
    last_update_date = models.DateTimeField(verbose_name=u'Fecha actualización')
    developer = models.ForeignKey(ServiceProvider, related_name=u'developer', verbose_name=u'Empresa desarrolladora', blank=True, null=True, on_delete=models.DO_NOTHING)
    maintainer =models.ForeignKey(ServiceProvider, related_name=u'maintainer', verbose_name=u'Empresa mantenimiento', blank=True, null=True, on_delete=models.DO_NOTHING)
    contract_end_date = models.DateTimeField(verbose_name=u'Fecha fin del contrato')
    size = models.IntegerField( verbose_name=u'Tamaño (#páginas)')
    visits = models.IntegerField( verbose_name=u'Visitas')
    analytics = models.CharField(verbose_name=u'Analytics', max_length=100)
    authentication =models.BooleanField(default=True, verbose_name=u'Tiene autenticación')
    site_type = models.ForeignKey(SiteType, verbose_name=u'Tipo de sitio', blank=True, null=True, on_delete=models.DO_NOTHING)
    content_type = models.ForeignKey(ContentType, verbose_name=u'Tipo de contenido', blank=True, null=True, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(State, verbose_name=u'Estado', blank=True, null=True, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, verbose_name=u'Categoría', blank=True, null=True, on_delete=models.DO_NOTHING)
    #SERVICIOS INTERNOS INTEGRADOS, SERVICIOS EXTERNOS INTEGRADOS
    services = models.ManyToManyField(Service, verbose_name=u'Servicios',  blank=True, null=True)
    location = models.ForeignKey(Location, verbose_name=u'Ubicación sitio desplegado', blank=True, null=True, on_delete=models.DO_NOTHING)
    Technology = models.ManyToManyField(Technology, verbose_name=u'Tecnologías', blank=True, null=True)
    design = models.CharField(verbose_name=u'Diseño', max_length=1000)
    audiences = models.ManyToManyField(Audience, verbose_name=u'Audiencias', blank=True, null=True)
    additional_info = models.CharField(verbose_name=u'Observaciones', max_length=1000)
    image = models.CharField(verbose_name=u'Imagen', max_length=1000)
    #TODO PROBLEMAS

    def natural_key(self):
        return dict(domain=self.domain, name=self.name, url=self.url_home)

    class Meta:
        verbose_name = u'Sitio'
        verbose_name_plural = u'Sitios'
        unique_together = ('name', 'domain', 'url_home')

    def __unicode__(self):
        return self.name + '_' + self.domain
