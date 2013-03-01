import doctest
import unittest

import txomon.ticket
from txomon.ticket.tests import api, model, query, wikisyntax, notification, \
                              conversion, report, roadmap, batch
from txomon.ticket.tests.functional import functionalSuite

def suite():
    suite = unittest.TestSuite()
    suite.addTest(api.suite())
    suite.addTest(model.suite())
    suite.addTest(query.suite())
    suite.addTest(wikisyntax.suite())
    suite.addTest(notification.suite())
    suite.addTest(conversion.suite())
    suite.addTest(report.suite())
    suite.addTest(roadmap.suite())
    suite.addTest(batch.suite())
    suite.addTest(doctest.DocTestSuite(txomon.ticket.api))
    suite.addTest(doctest.DocTestSuite(txomon.ticket.report))
    suite.addTest(doctest.DocTestSuite(txomon.ticket.roadmap))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
