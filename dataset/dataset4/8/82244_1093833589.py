def test_main():
    tests = [GeneralModuleTests, BasicTCPTest, TCPCloserTest, TCPTimeoutTest,
             TestExceptions, BufferIOTest, BasicTCPTest2, BasicUDPTest,
             UDPTimeoutTest, CreateServerTest, CreateServerFunctionalTest]

    tests.extend([
        NonBlockingTCPTests,
        FileObjectClassTestCase,
        UnbufferedFileObjectClassTestCase,
        LineBufferedFileObjectClassTestCase,
        SmallBufferedFileObjectClassTestCase,
        UnicodeReadFileObjectClassTestCase,
        UnicodeWriteFileObjectClassTestCase,
        UnicodeReadWriteFileObjectClassTestCase,
        NetworkConnectionNoServer,
        NetworkConnectionAttributesTest,
        NetworkConnectionBehaviourTest,
        ContextManagersTest,
        InheritanceTest,
        NonblockConstantTest
    ])
    tests.append(BasicSocketPairTest)
    tests.append(TestUnixDomain)
    tests.append(TestLinuxAbstractNamespace)
    tests.extend([TIPCTest, TIPCThreadableTest])
    tests.extend([BasicCANTest, CANTest])
    tests.extend([BasicRDSTest, RDSTest])
    tests.append(LinuxKernelCryptoAPI)
    tests.append(BasicQIPCRTRTest)
    tests.extend([
        BasicVSOCKTest,
        ThreadedVSOCKSocketStreamTest,
    ])
    tests.append(BasicBluetoothTest)
    tests.extend([
        CmsgMacroTests,
        SendmsgUDPTest,
        RecvmsgUDPTest,
        RecvmsgIntoUDPTest,
        SendmsgUDP6Test,
        RecvmsgUDP6Test,
        RecvmsgRFC3542AncillaryUDP6Test,
        RecvmsgIntoRFC3542AncillaryUDP6Test,
        RecvmsgIntoUDP6Test,
        SendmsgUDPLITETest,
        RecvmsgUDPLITETest,
        RecvmsgIntoUDPLITETest,
        SendmsgUDPLITE6Test,
        RecvmsgUDPLITE6Test,
        RecvmsgRFC3542AncillaryUDPLITE6Test,
        RecvmsgIntoRFC3542AncillaryUDPLITE6Test,
        RecvmsgIntoUDPLITE6Test,
        SendmsgTCPTest,
        RecvmsgTCPTest,
        RecvmsgIntoTCPTest,
        SendmsgSCTPStreamTest,
        RecvmsgSCTPStreamTest,
        RecvmsgIntoSCTPStreamTest,
        SendmsgUnixStreamTest,
        RecvmsgUnixStreamTest,
        RecvmsgIntoUnixStreamTest,
        RecvmsgSCMRightsStreamTest,
        RecvmsgIntoSCMRightsStreamTest,
        # These are slow when setitimer() is not available
        InterruptedRecvTimeoutTest,
        InterruptedSendTimeoutTest,
        TestSocketSharing,
        SendfileUsingSendTest,
        SendfileUsingSendfileTest,
    ])
    tests.append(TestMSWindowsTCPFlags)

    thread_info = support.threading_setup()
    support.run_unittest(*tests)
    support.threading_cleanup(*thread_info)