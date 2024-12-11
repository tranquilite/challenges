""" Bare masse fucka tester av shorts.
Er egentlig bare testcasene som er oppgitt i problembeskrivelsen"""
import unittest
import shorts as task
import utility


class CodonConversion(unittest.TestCase):
    """Same-same. Super not implemented."""
    def test_conversion(self):
        self.assertTrue(isinstance(utility.rna_codon_map_conversion(), dict))


class ProteinMap(unittest.TestCase):
    """Super not implemented yet"""
    def test_protein_map(self):
        self.assertTrue(isinstance(utility.rna_codon_map_conversion(), dict))


class FASTAParser(unittest.TestCase):
    TESTSETT = \
        """>Rosalind_1\n""" + \
        """ATCCAGCT\n""" + \
        """>Rosalind_2\n""" + \
        """GGGCAACT\n"""
    TESTSETT2 = 'ATCCAGCT\nGGGAACT\n'
    TESTCRIB = {
        'Rosalind_1': 'ATCCAGCT', 'Rosalind_2': 'GGGCAACT'
    }

    def test_fasta_parser(self):
        self.assertEqual(utility.parse_fasta_str(self.TESTSETT), self.TESTCRIB)

    def test_fasta_invalid(self):
        """with self.assertRaises(KeyError):  # Test om keyerror håndteres?
            utility.parse_fasta_str(self.TESTSETT2)"""
        self.assertEqual(utility.parse_fasta_str(self.TESTSETT2), {})


class REVC(unittest.TestCase):
    TESTSETT = """AAAACCCGGT"""
    TESTCRIB = """ACCGGGTTTT"""

    def test_revc_sample(self):
        self.assertEqual(
            task.REVC_complementing_a_strand_of_dna(self.TESTSETT),
            self.TESTCRIB
        )


class PROT(unittest.TestCase):
    TESTSETT = """AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"""
    TESTCRIB = """MAMAPRTEINSTRING"""

    def test_prot_sample(self):
        self.assertEqual(
            task.PROT_translating_rna_into_protein(self.TESTSETT),
            self.TESTCRIB
            )


class FIB(unittest.TestCase):
    TESTSETT = """5 3"""
    TESTCRIB = 19

    def test_fib_sample(self):
        self.assertEqual(
            task.FIB_rabbits_and_recurrence_relations(self.TESTSETT),
            self.TESTCRIB
        )


class GC(unittest.TestCase):
    TESTSETT = """>Rosalind_6404\n""" + \
        """CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG\n""" + \
        """>Rosalind_5959\n""" + \
        """CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC\n""" + \
        """>Rosalind_0808\n""" + \
        """CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT\n"""  # noqa: E501
    TESTCRIB = ('Rosalind_0808', 60.919540)

    def test_gc_sample_0(self):
        self.assertEqual(
            task.GC_computing_gc_content(self.TESTSETT)[0],
            self.TESTCRIB[0]
        )

    def test_gc_sample_1(self):
        """Rosalind allows for a default error of 0.001 (three places)"""
        self.assertAlmostEqual(
            task.GC_computing_gc_content(self.TESTSETT)[1],
            self.TESTCRIB[1], places=3
        )


class HAMM(unittest.TestCase):
    TESTSETT = """GAGCCTACTAACGGGAT\n""" + \
        """CATCGTAATGACGGCCT"""
    TESTCRIB = 7

    def test_hamm_sample(self):
        self.assertEqual(
            task.HAMM_Counting_point_mutations(self.TESTSETT),
            self.TESTCRIB
        )


class SUBS(unittest.TestCase):
    TESTSETT = ["""GATATATGCATATACTT""", """ATAT"""]
    TESTCRIB = """ 2 4 10"""

    def test_subs_sample(self):
        self.assertEqual(
            task.SUBS_Finding_a_motif_in_dna(*self.TESTSETT),
            self.TESTCRIB
        )


class CONS(unittest.TestCase):
    TESTSETT = \
        """>Rosalind_1\n""" + \
        """ATCCAGCT\n""" + \
        """>Rosalind_2\n""" + \
        """GGGCAACT\n""" + \
        """>Rosalind_3\n""" + \
        """ATGGATCT\n""" + \
        """>Rosalind_4\n""" + \
        """AAGCAACC\n""" + \
        """>Rosalind_5\n""" + \
        """TTGGAACT\n""" + \
        """>Rosalind_6\n""" + \
        """ATGCCATT\n""" + \
        """>Rosalind_7\n""" + \
        """ATGGCACT"""
    TESTCRIB = \
        """ATGCAACT\n""" + \
        """A: 5 1 0 0 5 5 0 0\n""" + \
        """C: 0 0 1 4 2 0 6 1\n""" + \
        """G: 1 1 6 3 0 1 0 0\n""" + \
        """T: 1 5 0 0 0 1 1 6\n"""

    def test_cons_sample(self):
        self.assertEqual(
            task.CONS_overlap_graphs(self.TESTSETT), self.TESTCRIB
        )
