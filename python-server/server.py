from spyne import Application, rpc, ServiceBase, Float, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class ProteinService(ServiceBase):
    @rpc(Float, Unicode, _returns=Float)
    def get_protein(ctx, weight_kg, intensity):
        intensity = intensity.lower()
        multiplier = {
            'low': 0.8,
            'moderate': 1.4,
            'high': 1.8
        }.get(intensity, 0.8)

        # Calculate protein intake in grams
        return weight_kg * multiplier

application = Application(
    [ProteinService],
    tns='http://proteincalculator.example.com/proteinservice',
    name='ProteinCalculatorService',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

if __name__ == '__main__':
    import logging
    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.INFO)
    logging.info("SOAP server starting...")

    wsgi_app = WsgiApplication(application)
    server = make_server('127.0.0.1', 8000, wsgi_app)
    
    logging.info("SOAP server running at http://127.0.0.1:8000/ProteinCalculatorService")
    logging.info("WSDL available at http://127.0.0.1:8000/ProteinCalculatorService?wsdl")
    
    server.serve_forever()
