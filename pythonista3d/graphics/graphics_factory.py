import platform
import configparser
import importlib
import inspect

from pythonista3d.graphics.graphics_delegate import GraphicsDelegate

APP_INI_LOCATION = 'pythonista3d/config/app.ini'


class GraphicsFactory(object):
  """
  Produces a graphics delegate object based on the platform on which the code is running.
  This is determined by the defaults for those platforms in a properties file.
  """
  
  @staticmethod
  def _make_graphics_inst(gconfig, system):
    """
    Create an instance of the graphics delegate for the user's system.
    Appropriate modules are defined in the app.ini then dynamically instantiated
    :param gconfig: the config file section for graphics
    :param system: the system the user is on
    :return: an instance of the appropriate class
    """
    if system == 'iOS':
      smod = gconfig['DefaultModulePythonista']
    elif system == 'Windows':
      smod = gconfig['DefaultModuleDesktop']
    else:
      raise Exception('Platform not supported: [%s]' % system)
    lib = importlib.import_module(smod)
    
    # inspect imported module for defined classes
    classes = [m[0] for m in inspect.getmembers(lib, inspect.isclass) if m[1].__module__ == smod]
    if len(classes) != 1:
      raise Exception('A graphics delegate module should contain one, and only one, delegate class definition.')
      
    # get class object and return a fresh instance
    cls = getattr(lib, classes[0])
    return cls()

  @staticmethod
  def get_delegate() -> "GraphicsDelegate":
    """
    Detect the type of system the user is on
    :return: the appropriate graphics delegate
    """
    if platform.system() == 'Darwin':  #iOS
      system = 'iOS'
    elif platform.system() == 'Windows':
      system = 'Windows'
    
    config = configparser.ConfigParser()
    config.read(APP_INI_LOCATION)
    graphics_config = config['graphics']
    return GraphicsFactory._make_graphics_inst(graphics_config, system)

