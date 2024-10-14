import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='')
_log = logging.getLogger(__name__)

# # int
# # -----------------------------------------
# int1 = 2342134213421341234213421342134123423142314234213412342134213421342134123423142134
# int2 = int('2')
# int3 = 2_342_134_213_421_341_234_213_421_342_134_123_423_142_314_234_213_412_342_134_213_421_342_134_133_423_142_137
# _log.info(f'{int1 + int2 + int3:_}')

# float
# -----------------------------------------
fl1 = 1.1
_log.info(fl1)
fl_exp = 0.0000000000000000000000005
_log.info(fl_exp)  # 5*(10**-25)
_log.info(f'{5 * (10 ** -25):.25f}')
_log.info(f'{fl_exp:.25f}')

fl1 = float('1.1')
fl2 = float('2.2')
_log.info(fl1 + fl2)
#
# fl3 = float(1.0)
# fl4 = float(7.0)
# _log.info(fl3 / fl4)

# decimal
# -----------------------------------------
from decimal import getcontext, Decimal

getcontext().prec = 17
_log.info(Decimal(1) / Decimal(7))
getcontext().prec = 30
_log.info(Decimal(1) / Decimal(7))

# float number stored as object by python first
# then only we do convert python float -> to Decimal
_log.info(Decimal(1.101) + Decimal(2.20200))

# all operations including str-> Decimal convert
# will be inside Decimal object logic
_log.info(Decimal('1.101') + Decimal('2.20200'))


