#! /usr/bin/env python
# coding:utf8

# from getEntry import GetEntry
# import searchAccesion

from Bio.Blast.Applications import NcbiblastxCommandline
import os.path
import os


#BLASTPATH = "Please change your blast path"


def createDB(fastaFileName, dbFileName, dbType="prot"):
    toolPath = "makeblastdb"
    command = " ".join(
        [toolPath, "-in", fastaFileName, "-dbtype", dbType, "-out", dbFileName])
    os.system(command)


def blastp(queryFileName, dbFileName, outFileName):
    comline = NcbiblastxCommandline(query=queryFileName, db=dbFileName, out=outFileName,
                                    cmd="blastp", evalue=0.001, outfmt=5, num_alignments=1)
    stdout, stderr = comline()
    return stdout, stderr


if __name__ == '__main__':

    queryFileName="../t2/protein.fa"
    dbFileName="db/p"
    outFileName="res/result.xml"

    createDB(queryFileName, dbFileName)
    stdout, stderr = blastp(queryFileName, dbFileName, outFileName)

