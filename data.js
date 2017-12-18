code_hierarchy_data = [
    "", 
// total Cases and SARs   Cases then alerts then sars  
	[
        4500, 
        290,
		200
    ], 
//First Rules group type alerts, sars  
	{
        "Structuring": [
            "Structuring", 
            [
                1000, 
                250,
				100
            ], 
			//Subtype(child of) first rule more granular
            {
                "New Account >4k": [
                    "New Account >4k", 
                    [
                       500, 
                        15,
						70
                    ], 
                    {}
				],
                "Cash >4k with in 29 days new account": [
                    "Cash >4k with in 29 days new account", 
                    [
                        500, 
                        10,
						50
                    ], 
						{
							"Personal >4k with in 29 days": [
								"Personal >4k with in 29 days",
								[
								250,
								5,
								40
								],
									{
											"California Branches": [
										"California Branches",
										[
										150,
										3,
										30
										],
											{
													"Northern California Branches": [
														"Northern California Branches",
														[
														100,
														2,
														10
														],
														{}
														],
													"Southern California Branches": [
														"Southern California Branches",
														[
														50,
														1,
														20
														],
														{}
														],														
											}
										],
											"Colorado Branches": [
										"Colorado Branches",
										[
										100,
										2,
										10
										],
										{}
										],										
									}
								],	
							"Non Personal >4k with in 29 days": [
								"Non Personal >4k with in 29 days",
								[
								250,
								5,
								10
								],
								{}
								],									
						}
				],
				
				}
			],
			"Round Dollar Amount": [
            "Round Dollar Amount", 
				[
                1000, 
                250,
				100
				], 
					{
					//Subtype(child of) first rule more granular
						"RND sending to VS/S Country": [
							"RND sending to VS/S Country", 
							[
							   500, 
								15,
								10
							], 
							{
							
									//first subtype of the second subtype of first rule more granual
										"Personal RND sending to a  VS/S Country": [
										"Personal RND sending to a  VS/S Country", 
										[
										250, 
										5,
										2
										],								
										{}
										],
									//second subtype of the second subtype of first rule more granual
										"Personal RND sending to a  VS/S Country": [
										" Personal RND sending toa  VS/S Country", 
										[
										250, 
										5,
										2
										],								
												{
													//first subtype of the second subtype of the second subtype of the first rule more granual
													"Personal RND sending to a  VS Country": [
													"Personal RND sending to a  VS Country", 
													[
														150, 
														2,
														1
													],								
													{}
													],												
													//first subtype of the second subtype of the second subtype of the first rule more granual
													"Personal RND sending to a  S Country": [
													"Personal RND sending to a  S Country", 
													[
														100, 
														3,
														1
													],								
													{}
													],													
												
												
												
												}
										],		
							
							
							}
							],
					//Second subtyp of first rule more granual
						"RND credit from a  VS/S Country": [
							"RND credit from a  VS/S Country", 
								[	
									500, 
									10,
									5
								], 
								{
								
									//first subtype of the second subtype of first rule more granual
										"Personal RND credit from a  VS/S Country": [
										"Personal RND credit from a  VS/S Country", 
										[
										250, 
										5,
										2
										],								
										{}
										],
									//second subtype of the second subtype of first rule more granual
										"Non Personal RND credit from a  VS/S Country": [
										"Non Personal RND credit from a  VS/S Country", 
										[
										250, 
										5,
										2
										],								
												{
													//first subtype of the second subtype of the second subtype of the first rule more granual
													"Non-Personal RND credit from a  VS Country": [
													"Non-Personal RND credit from a  VS Country", 
													[
														150, 
														2,
														1
													],								
													{}
													],												
													//first subtype of the second subtype of the second subtype of the first rule more granual
													"Non-Personal RND credit from a  S Country": [
													"Non-Personal RND credit from a  S Country", 
													[
														100, 
														3,
														1
													],								
													{}
													],													
												
												
												
												}
										],										
								}
								],
					}
			],

				
			"SOMI": [
            "SOMI", 
            [
                1000, 
                250,
				100
            ], 
			//Subtype(child of) first rule more granular
            {
                "SOMI > 25k": [
                    "SOMI > 25k", 
                    [
                       500, 
                        150,
						50
                    ], 
                    {}
				],
                "SOMI >50k": [
                    "SOMI >50k", 
                    [
                        500, 
                        100,
						50
                    ], 
                    {}
				],

				}
			],
			"RDC": [
            "RDC", 
            [
                1000, 
                250,
				100
            ], 
			//Subtype(child of) first rule more granular
            {
                "Moble RDC": [
                    "Mobile RDC", 
                    [
                       500, 
                        150,
						90
                    ], 
                    {}
				],
                "Business RDC": [
                    "Business RDC", 
                    [
                        500, 
                        100,
						10
                    ], 
                    {}
				],

				}
			],
			
		"FTF ": [
			"Flow Through Funds",
				[
					500,
					5,
					6
				],
				{}
				],	
			
			
			
		}
	]
