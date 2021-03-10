
import sys
sys.path.append('../')
sys.path.append('.')

from service import Service

def test_service_call_counts():
    """Tests counts based on number of calls to both services."""
    service = Service()
    for i in range(3):
        service.service1()
    for i in range(8):
        service.service2()
    for i in range(2):
        service.service1()
    for i in range(6):
        service.service2()
    assert service.num_calls() == (3 + 2, 8 + 6)
