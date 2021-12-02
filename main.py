from py_crypto_hd_wallet import HdWalletSaver, HdWalletBip44Coins, HdWalletBipFactory, HdWalletBip, HdWalletBipWordsNum, HdWalletMoneroCoins, HdWalletMoneroFactory


print("auto wallet crypto generator")
# print("supported coins : BITCOIN, DOGECOIN, ETHEREUM_CLASSIC, LITECOIN, KAVA, BINANCE, BINANCE_CHAIN, COSMOS, BITCOIN_SV")

coinlist = ['BITCOIN', 'BITCOIN_TEST', 'ETHEREUM','ETHEREUM_CLASSIC', 'DOGECOIN', 'LITECOIN', 'KAVA', 'BINANCE_CHAIN', 'COSMOS', 'BITCOIN_SV', 'ALGORAND', 'AVAX_C_CHAIN',
            'AVAX_P_CHAIN', 'AVAX_X_CHAIN', 'BAND_PROTOCOL', 'BINANCE_SMART_CHAIN', 'BITCOIN_CASH', 'DASH', 'ELROND', 'EOS', 'FANTOM_OPERA', 'FILECOIN', 'HARMONY_ONE_ATOM',
            'HARMONY_ONE_ETH', 'HARMONY_ONE_METAMASK', 'HUOBI_CHAIN', 'IRIS_NET', 'KUSAMA_ED25519_SLIP', 'OKEX_CHAIN_ATOM', 'OKEX_CHAIN_ETH', 'OKEX_CHAIN_ATOM_OLD', 'NANO',
            'NEO', 'ONTOLOGY', 'POLKADOT_ED25519_SLIP', 'POLYGON', 'RIPPLE', 'SOLANA', 'STELLAR', 'TERRA', 'TEZOS', 'THETA', 'TRON','VECHAIN', 'ZCASH', 'ZILLIQA', 'MONERO_MAINNET']
# coin = input("Enter Coin name:")
# coin = coin.upper()
count = input("Enter the number of addresses:")
count = int(count)

for coin in coinlist:
    hd_wallet_fact = ''
    print("coin", coin)
    if coin == "BITCOIN":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN)
    elif coin == "BITCOIN_TEST":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN_TESTNET)
    elif coin == "ETHEREUM":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.ETHEREUM)
    elif coin == "ETHEREUM_CLASSIC":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.ETHEREUM_CLASSIC)
    elif coin == "DOGECOIN":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.DOGECOIN)
    elif coin == "LITECOIN":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.LITECOIN)
    elif coin == "KAVA":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.KAVA)
    elif coin == "BINANCE_CHAIN":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BINANCE_CHAIN)
    elif coin == "COSMOS":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.COSMOS)
    elif coin == "BITCOIN_SV":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN_SV)
    elif coin == "ALGORAND":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.ALGORAND)
    elif coin == "AVAX_C_CHAIN":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.AVAX_C_CHAIN)
    elif coin == "AVAX_P_CHAIN":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.AVAX_P_CHAIN)
    elif coin == "AVAX_X_CHAIN":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.AVAX_X_CHAIN)
    elif coin ==  "BAND_PROTOCOL":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BAND_PROTOCOL)
    elif coin == "BINANCE_SMART_CHAIN":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BINANCE_SMART_CHAIN)
    elif coin == "BITCOIN_CASH":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN_CASH)
    elif coin == "DASH":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.DASH)
    elif coin == "ELROND":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.ELROND)
    elif coin == "EOS":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.EOS)
    elif coin == "FANTOM_OPERA":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.FANTOM_OPERA)
    elif coin == "FILECOIN":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.FILECOIN)
    elif coin == "HARMONY_ONE_ATOM":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.HARMONY_ONE_ATOM)
    elif coin == "HARMONY_ONE_ETH":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.HARMONY_ONE_ETH)
    elif coin == "HARMONY_ONE_METAMASK":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.HARMONY_ONE_METAMASK)
    elif coin == "HUOBI_CHAIN":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.HUOBI_CHAIN)
    elif coin == "IRIS_NET":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.IRIS_NET)
    elif coin == "KUSAMA_ED25519_SLIP":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.KUSAMA_ED25519_SLIP)
    elif coin == "OKEX_CHAIN_ATOM":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.OKEX_CHAIN_ATOM)
    elif coin == "OKEX_CHAIN_ETH":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.OKEX_CHAIN_ETH)
    elif coin == "OKEX_CHAIN_ATOM_OLD":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.OKEX_CHAIN_ATOM_OLD)
    elif coin == "NANO":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.NANO)
    elif coin == "NEO":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.NEO)
    elif coin == "ONTOLOGY":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.ONTOLOGY)
    elif coin == "POLKADOT_ED25519_SLIP":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.POLKADOT_ED25519_SLIP)
    elif coin == "POLYGON":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.POLYGON)
    elif coin == "RIPPLE":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.RIPPLE)
    elif coin == "SOLANA":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.SOLANA)
    elif coin == "STELLAR":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.STELLAR)
    elif coin == "TERRA":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.TERRA)
    elif coin == "TEZOS":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.TEZOS)
    elif coin == "THETA":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.THETA)
    elif coin == "TRON":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.TRON)
    elif coin == "VECHAIN":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.VECHAIN)
    elif coin == "ZCASH":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.ZCASH)
    elif coin == "ZILLIQA":
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.ZILLIQA)
    elif coin == "MONERO_MAINNET":
        hd_wallet_fact = HdWalletMoneroFactory(HdWalletMoneroCoins.MONERO_MAINNET)
    else:
        print("error")
        exit()

    hd_wallet = hd_wallet_fact.CreateRandom(coin + "_wallet", HdWalletBipWordsNum.WORDS_NUM_24)
    hd_wallet.Generate(addr_num=count)
    HdWalletSaver(hd_wallet).SaveToFile(coin+".txt")






