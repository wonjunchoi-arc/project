from cctv.models import CctvDTO
from cctv.services import CctvService

class CctvApi():
    dto = CctvDTO()
    service = CctvService()

    while 1:
        menu = input('0.Exit 1.CSV 2.Excel 3.')
        if menu == '0':
            break
        elif menu == '1':
            dto.fname = service.new_model('cctv_in_seoul.csv')
            dto.fname =service.new_model('crime_in_seoul.csv')
            dto.fname =service.new_model('police_position.csv')
            dto.fname =service.new_model('us_unemployment.csv')
            service.print_dframe(dto.fname)

        elif menu == '2':
            service.new_model('pop_in_seoul.xls')
            service.print_dframe(dto.fname)




