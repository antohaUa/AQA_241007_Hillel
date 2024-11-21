# class Write:
#     def prn():
#         print('Hello World')
#         return 10
#
#
# print(Write.prn())
# # Write.prn()
# # #
# w1 = Write()
# # w2 = Write()
# # w3 = Write()
# # w4 = Write()
# print(w1.prn)
#
#
# # #
# # #
# # w1.prn()  # will return error cause we call as Write.prn(w1) but function has no parameters
# #
# # ##### self
# class Write2:
#
#     def prn(self):
#         print(self)
#         # breakpoint()
#         print('Hello World2')
# #
# #
# w2 = Write2()
# print(hex(id(w2)))
# print(id(w2))
# w2.prn() # identical to Write2.prn(w2)
#
#
#
#
# self usage as access to local variables ability to create them

class Vehicle:

    def beep(self):
        if not hasattr(self, 'beep_count'):
            self.beep_count = 0
        self.beep_count += 1


v1 = Vehicle()
v1.beep() # ==  Vehicle.beep(v1)
v1.beep()
Vehicle.beep(v1)
Vehicle.beep(v1)
print(v1.__dict__)
print(Vehicle.__dict__)
# v2 = Vehicle()
# v2.beep() # ==  Vehicle.beep(v2)
# v2.beep()
# v2.beep()
# v2.beep()
# v2.beep()
# v3 = Vehicle()
# print(f'{v1.beep_count=}')
# print(f'{v2.beep_count=}')
# print(v1.__dict__)
# print(v2.__dict__)
# print(v3.__dict__)

