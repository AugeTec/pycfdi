from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from simple_cfdi.spec import Comprobante, CFDI_4_0_SCHEMA_LOCATION, CFDI_4_0_NAMESPACES


def import_xml(xml_data: bytes) -> Comprobante:
    """ Import xml_data into Comprobante class """
    xml_parser = XmlParser()
    comprobante = xml_parser.from_bytes(xml_data, Comprobante)

    return comprobante


def export_xml(comprobante: Comprobante) -> bytes:
    """ Export Comprobante class into xml_data """
    serializer_config = SerializerConfig(
        schema_location=CFDI_4_0_SCHEMA_LOCATION,
    )

    serializer = XmlSerializer(config=serializer_config)
    xml_data = serializer.render(comprobante, ns_map=CFDI_4_0_NAMESPACES)

    return xml_data
