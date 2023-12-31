class DB_MODIFIER:
    # dart
    def get_md_dart_fundamental_df(self, dart_fundamental_df):
        rename_dict = {
            "stock_code": "StockCode",
            "fs_nm": "FSName",
            "account_nm": "AccountName",
            "thstrm_amount": "Amount",
        }
        dart_fundamental_df["ReprtInfo"] = dart_fundamental_df.apply(lambda x: x.bsns_year + "_" + x.reprt_code, axis=1)
        using_columns = list(rename_dict.values()) + ["ReprtInfo"]
        md_dart_fundamental_df = self._get_renamed_df(dart_fundamental_df, rename_dict)
        md_dart_fundamental_df = self._get_sliced_df(md_dart_fundamental_df, using_columns)
        return md_dart_fundamental_df

    # dart
    def get_md_dart_info_df(self, dart_info_df):
        rename_dict = {
            "stock_code": "StockCode",
            "corp_name": "StockName",
            "sector": "Sector",
            "product": "Product",
        }
        using_columns = list(rename_dict.values())
        md_dart_info_df = self._get_renamed_df(dart_info_df, rename_dict)
        md_dart_info_df = self._get_sliced_df(md_dart_info_df, using_columns)
        return md_dart_info_df

    # fdr
    def get_md_fdr_ohlcv_df(self, fdr_ohlcv_df):
        md_fdr_ohlcv_df = fdr_ohlcv_df.copy()
        return md_fdr_ohlcv_df

    # fdr
    def get_md_fdr_info_df(self, fdr_info_df):
        rename_dict = {
            "Code": "StockCode",
            "Name": "StockName",
            "Market": "Market",
            "Stocks": "Shares",
        }
        using_columns = list(rename_dict.values())
        md_fdr_info_df = self._get_renamed_df(fdr_info_df, rename_dict)
        md_fdr_info_df = self._get_sliced_df(md_fdr_info_df, using_columns)
        return md_fdr_info_df

    # pykrx
    def get_md_pykrx_info_df(self, pykrx_info_df):
        rename_dict = {
            "날짜": "Date",
        }
        md_pykrx_info_df = self._get_renamed_df(pykrx_info_df, rename_dict)
        return md_pykrx_info_df

    # krx
    def get_md_krx_info_df(self, krx_info_df):
        rename_dict = {
            "종목코드": "StockCode",
            "시장구분": "MarketName",
            "업종명": "SectorName",
        }
        using_columns = list(rename_dict.values())
        md_KRX_sector_df = self._get_renamed_df(krx_info_df, rename_dict)
        md_KRX_sector_df = self._get_sliced_df(md_KRX_sector_df, using_columns)
        return md_KRX_sector_df

    @staticmethod
    def _get_renamed_df(df, rename_dict):
        renamed_df = df.rename(columns=rename_dict)
        return renamed_df

    @staticmethod
    def _get_sliced_df(df, using_columns):
        sliced_df = df.loc[:, using_columns]
        return sliced_df
