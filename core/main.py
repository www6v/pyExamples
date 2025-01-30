import basic
import basic_ref as br
import basic_iter as bi
import coroutine as co

import basic_collection as bc
from basic_collection import Scheduler


class MainClass:

    def basicFunc(self):
        basic.ifAndLoop()
        # basic.errerHandling()
        basic.errorHandling1()
        basic.compare()

    def dataType(self):
        s = Scheduler()
        s.abort_seq_group()


        # bc.listFunc()
        # bc.tupleFunc()
        # bc.dictFunc()
        # bc.setFunc()


        # bc.shallowCopy()
        # bc.shallowCopy1()
        # bc.deepcopy()    

    def otherFunc(self):
        br.reference()
        br.reference1()

        bi.iter_test()
        bi.test_iterator()
        bi.test_generator()
        co.asynRun()
        co.asynRun1()    

if __name__ == '__main__':
    m = MainClass()

    # m.basicFunc()
    m.dataType()  
    # m.otherFunc()


