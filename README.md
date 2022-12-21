# AEI-CLAB Cura Profiles

Repositorio para el proyecto AEI-CLAB. Entregable de FabLab Barcelona conteniendo los perfiles de configuración de CURA para la [impresora de pasta de biomateriales](https://github.com/fablabbcn/aei-kit-impresion-pasta) y una copia del proyecto opensource de [slicer de Cura 5.2.1](https://github.com/Ultimaker/Cura). Los archivos de configuración ya no son necesarios para una instalación manual de la impresora, ya que viene por defecto incluido en el descargable del programa Cura a partir de la version 5.2.2.


## Resumen de AEI-CLAB

El objetivo de este proyecto es promover el uso de la tecnología maker y la impresión 3D en el ámbito educativo, utilizando materiales sostenibles y biocompatibles como la pasta de biomateriales.
La impresión 3D es una técnica de fabricación aditiva que permite la creación de objetos tridimensionales a partir de un modelo digital. Esta tecnología está revolucionando diversos campos, desde la industria hasta la medicina y la educación.

El uso de la impresión 3D en la educación permite a los estudiantes desarrollar habilidades técnicas y creativas, así como comprender conceptos científicos y tecnológicos de manera práctica y amena. Además, la utilización de biomateriales en la impresión 3D contribuye a la sostenibilidad y al desarrollo de soluciones innovadoras y responsables con el medio ambiente.
Este proyecto incluye talleres y actividades prácticas dirigidos a estudiantes de nivel secundario y universitario, en los que se enseñan los fundamentos de la impresión 3D y se explorarán las posibilidades de la pasta de biomateriales como material de impresión. Los participantes tendrán la oportunidad de diseñar y fabricar sus propios objetos utilizando esta tecnología, fomentando así su creatividad e innovación.
Esperamos que este proyecto contribuya a la formación de una nueva generación de jóvenes comprometidos con la sostenibilidad y la tecnología, y que promueva el uso de la impresión 3D como herramienta educativa y de innovación.

## Instalación de perfiles o software CURA con compatibilidad para la impresora de pasta y biomateriales

Si ya tiene instalado CURA y la impresora de pasta de biomateriales no está disponible en el menú de añadir una nueva impresora bajo "FABLABBCN---PASTE PRINTER" y no está en la lista de impresoras compatibles, puede seguir esta guía para instalar perfiles de máquina para su slicer cura.

Para configurar su impresora, necesita al menos 2 tipos de archivos que llamamos archivos de definición:

     - Un archivo de definición de máquina que define los atributos de su máquina. Puedes usar esto como una plantilla. Para obtener más detalles, puede consultar la página [Archivos de definición de máquinas](https://github.com/Ultimaker/Cura/wiki/Adding-new-machine-profiles-to-Cura).
     - Un archivos de definición de extrusor que definen los atributos del extrusor en su máquina. Si su máquina solo tiene 1 extrusora, entonces solo necesita 1 archivo de definición de extrusora,como es esta caso. Consulte la página [Archivos de definición de máquinas](https://github.com/Ultimaker/Cura/wiki/Adding-new-machine-profiles-to-Cura) para obtener más detalles.

Una vez se haya descargado ambos perfiles, coloque el perfil qe *definición de máquina* en la carpeta de  **recursos/definiciones**, o en **definiciones**, en la carpeta de configuración del usuario dónde esté instalado Cura.
Para los archivos de *definición de extrusores*, debe colocarlos en recursos/extrusores, o en los extrusores, en la carpeta de configuración del usuario dónde esté instalado Cura.



Este repositorio contiene:

- Archivo de definición de impresora[link](PastePrinter_machine_extruder_Definitions/fablabbcn_pasteprinter.def.json)
- Archivo de configuración de extrusor[link](PastePrinter_machine_extruder_Definitions/fablabbcn_0.def.json)
- Mirror de todos los [archivos instalables](Cura 5.2.1) de CURA VERSION 5.2.1


## Descarga de Cura

Aquí puedes encontrar los links de descarga de [CURA](https://ultimaker.com/es/software/ultimaker-cura) 5.2.1 para distintos sistemas operativos:

Descarga para windows [link](https://github.com/Ultimaker/Cura/releases/download/5.2.1/Ultimaker-Cura-5.2.1-win64.exe)
Descarga para MACOS [link](https://github.com/Ultimaker/Cura/releases/download/5.2.1/Ultimaker-Cura-5.2.1-mac.dmg)
Descarga para Linux [link](https://github.com/Ultimaker/Cura/releases/download/5.2.1/Ultimaker-Cura-5.2.1-linux.AppImage)


## Créditos

Este complemento fue creado por Eduardo Chamorro Martin para FabLab Barcelona en el IAAC (Instituto de Arquitectura Avanzada de Cataluña),en el contexto del programa de ayudas para el apoyo a agrupaciones empresariales innovadoras del Ministerio de Industria, Comercio y Turismo. Convocatoria 2022.

Bajo el proyecto **CLAB: INNOVACIÓN EN PROCESOS DE FABRICACIÓN CIRCULAR Y ABIERTA PARA ENTORNOS EDUCATIVOS**

Partners del proyecto:

- IAAC & FabLab Barcelona
- Fundación Bofill  
- Kid's Cluster
- Abacus cooperativa
- Esteam education
- Anthesis Lavola


## Agradecimientos

-Santi Fuentemilla & Guillem Camprodon por coordinar y apoyar este proyecto.


## Licencia

Estos diseños son de código abierto bajo licencia CERN Open Hardware Licence v1.2 para más detalles puedes consultar la [licencia completa](LICENSE)
