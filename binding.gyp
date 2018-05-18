{
    "targets": [
        {
            "target_name": "nodex16r",
            "sources": [
                "multihashing.cc",
                "sha3/aes_helper.c",
                "sha3/sph_blake.c",
                "sha3/sph_bmw.c",
                "sha3/sph_cubehash.c",
                "sha3/sph_echo.c",
                "sha3/sph_groestl.c",
                "sha3/sph_jh.c",
                "sha3/sph_keccak.c",
                "sha3/sph_luffa.c",
                "sha3/sph_shavite.c",
                "sha3/sph_simd.c",
                "sha3/sph_skein.c",
                "sha3/sph_whirlpool.c",
                "sha3/sph_shabal.c",
                "sha3/hamsi.c",
		        "sha3/sha2.c",
		        "x16r.c",
            ],
            "cflags_cc": [
                "-std=c++11"
            ],
        }
    ]
}
