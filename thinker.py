
import warnings
warnings.filterwarnings("ignore", message=r"\[W008\]", category=UserWarning)
from collections import Counter
import asyncio
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re
import spacy
import RAKE
import time
from heapq import nlargest
import sqlite3
import collections
import os.path
from snippets.models import Snippet
from os import path
import os
import sys
import json
import io
import config

async def go(code):
    nlp = config.nlp
    stop = config.stop
    text = code
    corp_list, PROPN_list, sentences_list, combined_thoughts = [], [], [], []
    corp_list, bi_list, tri_list, rake_list = [], [], [], []
    text_list = text.splitlines()
    for line in text_list:
        line = re.sub('<.*?>', '', line)      
        corp_list.append(line)

    art_title = corp_list[0]
    nlp_title = nlp(art_title)

    if len(nlp_title) > 15:
        tit_sent_list = []
        for tit_sent in nlp_title.sents:
            tit_sent_list.append(tit_sent)   
        nlp_title = nlp(tit_sent_list[0].text)

        if len(nlp_title) > 15:
            cut_0 = nlp_title[0:14]
            nlp_title = nlp(cut_0.text)

    text_title = nlp_title.text
    PROPN_list.append(text_title)
    corp_list_joined = ' '.join(corp_list)  
    doc = nlp(corp_list_joined)

    wordsCL = []
    for token in doc:
        wordsCL.append(token.text)
    word_count = str(len(wordsCL))
    wordsCL = [word for word in wordsCL if len(word) > 1]
    wordsCL = [word.lower() for word in wordsCL]
    wordsCL = [word for word in wordsCL if word not in stop and word.isalpha()]

    adult = config.adult 
    adult_breast_enlargement = config.adult_breast_enlargement 
    adult_condoms = config.adult_condoms 
    adult_contraception = config.adult_contraception 
    adult_erection = config.adult_erection 
    adult_prostitution = config.adult_prostitution 
    animals_animals = config.animals_animals 
    animals_birds = config.animals_birds 
    animals_cats = config.animals_cats 
    animals_dogs = config.animals_dogs 
    animals_exotic_animals = config.animals_exotic_animals 
    animals_exotic_pets = config.animals_exotic_pets 
    animals_fish_aquaria = config.animals_fish_aquaria 
    animals_horses = config.animals_horses 
    animals_pet_food = config.animals_pet_food 
    animals_pet_products = config.animals_pet_products 
    animals_pet_supplies = config.animals_pet_supplies 
    animals_pets = config.animals_pets 
    animals_pets_amphibians = config.animals_pets_amphibians 
    animals_pets_fish = config.animals_pets_fish 
    animals_pets_rabbits = config.animals_pets_rabbits 
    animals_pets_reptiles = config.animals_pets_reptiles 
    animals_pets_rodents = config.animals_pets_rodents 
    animals_veterinarians = config.animals_veterinarians 
    animals_wildlife = config.animals_wildlife 
    arts_acting = config.arts_acting 
    arts_animation = config.arts_animation 
    arts_anime = config.arts_anime 
    arts_architecture = config.arts_architecture 
    arts_art_galleries = config.arts_art_galleries 
    arts_art_museums = config.arts_art_museums 
    arts_arts = config.arts_arts 
    arts_audio_equipment = config.arts_audio_equipment 
    arts_bars_listings = config.arts_bars_listings 
    arts_blues_music = config.arts_blues_music 
    arts_cartoons = config.arts_cartoons 
    arts_cd_shopping = config.arts_cd_shopping 
    arts_celebrities = config.arts_celebrities 
    arts_circus = config.arts_circus 
    arts_classical_music = config.arts_classical_music 
    arts_clubs_listings = config.arts_clubs_listings 
    arts_coloring = config.arts_coloring 
    arts_comics = config.arts_comics 
    arts_concerts = config.arts_concerts 
    arts_conventions = config.arts_conventions 
    arts_country_music = config.arts_country_music 
    arts_dance_electronic_music = config.arts_dance_electronic_music 
    arts_design = config.arts_design 
    arts_digital_art = config.arts_digital_art 
    arts_drawing = config.arts_drawing 
    arts_entertainment = config.arts_entertainment 
    arts_entertainment_industry = config.arts_entertainment_industry 
    arts_events_listings = config.arts_events_listings 
    arts_experimental_music = config.arts_experimental_music 
    arts_expos = config.arts_expos 
    arts_festivals = config.arts_festivals 
    arts_film_festivals = config.arts_film_festivals 
    arts_film_industry = config.arts_film_industry 
    arts_flash_trivia = config.arts_flash_trivia 
    arts_funny_pictures = config.arts_funny_pictures 
    arts_funny_videos = config.arts_funny_videos 
    arts_hip_hop = config.arts_hip_hop 
    arts_humor = config.arts_humor 
    arts_image_galleries = config.arts_image_galleries 
    arts_industrial_music = config.arts_industrial_music 
    arts_jazz_music = config.arts_jazz_music 
    arts_magic = config.arts_magic 
    arts_manga = config.arts_manga 
    arts_memes = config.arts_memes 
    arts_movie_showtimes = config.arts_movie_showtimes 
    arts_movie_soundtracks = config.arts_movie_soundtracks 
    arts_movies = config.arts_movies 
    arts_music = config.arts_music 
    arts_music_downloads = config.arts_music_downloads 
    arts_music_instruction = config.arts_music_instruction 
    arts_music_instruction_bass = config.arts_music_instruction_bass 
    arts_music_instruction_drums = config.arts_music_instruction_drums 
    arts_music_instruction_keyboard = config.arts_music_instruction_keyboard 
    arts_music_instrument_guitar = config.arts_music_instrument_guitar 
    arts_music_reference = config.arts_music_reference 
    arts_music_streams = config.arts_music_streams 
    arts_music_videos = config.arts_music_videos 
    arts_nightlife = config.arts_nightlife 
    arts_occult = config.arts_occult 
    arts_offbeat = config.arts_offbeat 
    arts_online_media = config.arts_online_media 
    arts_online_video = config.arts_online_video 
    arts_opera = config.arts_opera 
    arts_painting = config.arts_painting 
    arts_paranormal = config.arts_paranormal 
    arts_performing_arts = config.arts_performing_arts 
    arts_photgraphy = config.arts_photgraphy 
    arts_political_humor = config.arts_political_humor 
    arts_pop_music = config.arts_pop_music 
    arts_radio_music = config.arts_radio_music 
    arts_recording_industry = config.arts_recording_industry 
    arts_religious_music = config.arts_religious_music 
    arts_rock_music = config.arts_rock_music 
    arts_surveys = config.arts_surveys 
    arts_trivia = config.arts_trivia 
    arts_tv = config.arts_tv 
    arts_tv_commercials = config.arts_tv_commercials 
    arts_tv_industry = config.arts_tv_industry 
    arts_tv_shows = config.arts_tv_shows 
    arts_visual_art = config.arts_visual_art 
    beauty_beauty = config.beauty_beauty 
    beauty_beauty_pageants = config.beauty_beauty_pageants 
    beauty_body_art = config.beauty_body_art 
    beauty_body_care = config.beauty_body_care 
    beauty_cosmetic_procedures = config.beauty_cosmetic_procedures 
    beauty_cosmetic_surgery = config.beauty_cosmetic_surgery 
    beauty_cosmetics = config.beauty_cosmetics 
    beauty_cosmetology = config.beauty_cosmetology 
    beauty_exercise = config.beauty_exercise 
    beauty_exercise_equipment = config.beauty_exercise_equipment 
    beauty_face_care = config.beauty_face_care 
    beauty_fashion = config.beauty_fashion 
    beauty_fashion_collections = config.beauty_fashion_collections 
    beauty_fitness = config.beauty_fitness 
    beauty_fitness_antioxidants = config.beauty_fitness_antioxidants 
    beauty_hair_care = config.beauty_hair_care 
    beauty_hair_loss = config.beauty_hair_loss 
    beauty_hair_removal = config.beauty_hair_removal 
    beauty_hygiene_products = config.beauty_hygiene_products 
    beauty_massage = config.beauty_massage 
    beauty_nail_care = config.beauty_nail_care 
    beauty_perfumes = config.beauty_perfumes 
    beauty_skin_care = config.beauty_skin_care 
    beauty_spas = config.beauty_spas 
    beauty_weight_loss = config.beauty_weight_loss 
    books_books = config.books_books 
    books_children_books = config.books_children_books 
    books_e_books = config.books_e_books 
    books_fan_fiction = config.books_fan_fiction 
    books_literary_classics = config.books_literary_classics 
    books_poetry = config.books_poetry 
    books_writers_resources = config.books_writers_resources 
    business_advertising = config.business_advertising 
    business_aerospace = config.business_aerospace 
    business_affiliate_marketing = config.business_affiliate_marketing 
    business_agricultural_equipment = config.business_agricultural_equipment 
    business_agriculture = config.business_agriculture 
    business_alternative_energy = config.business_alternative_energy 
    business_automotive_industry = config.business_automotive_industry 
    business_biotech_industry = config.business_biotech_industry 
    business_business = config.business_business 
    business_business_capital = config.business_business_capital 
    business_business_consulting = config.business_business_consulting 
    business_business_education = config.business_business_education 
    business_business_fire_security = config.business_business_fire_security 
    business_business_management = config.business_business_management 
    business_business_operations = config.business_business_operations 
    business_business_plans = config.business_business_plans 
    business_business_presentations = config.business_business_presentations 
    business_business_services = config.business_business_services 
    business_business_venture = config.business_business_venture 
    business_chemical_industry = config.business_chemical_industry 
    business_cleaning_agents_industry = config.business_cleaning_agents_industry 
    business_commercial_vehicle = config.business_commercial_vehicle 
    business_construction = config.business_construction 
    business_construction_materials = config.business_construction_materials 
    business_corporate_events = config.business_corporate_events 
    business_defense_technology = config.business_defense_technology 
    business_delivery_industry  = config.business_delivery_industry  
    business_e_commerce = config.business_e_commerce 
    business_editing_services = config.business_editing_services 
    business_electricity_services = config.business_electricity_services 
    business_energy_industry = config.business_energy_industry 
    business_event_planning = config.business_event_planning 
    business_finance_industry = config.business_finance_industry 
    business_food_service = config.business_food_service 
    business_forestry_industry = config.business_forestry_industry 
    business_freight_industry = config.business_freight_industry 
    business_gas_industry = config.business_gas_industry 
    business_heavy_equipment_industry = config.business_heavy_equipment_industry 
    business_hospitality_industry = config.business_hospitality_industry 
    business_hospitality_planning = config.business_hospitality_planning 
    business_industrial_equipment = config.business_industrial_equipment 
    business_industry = config.business_industry 
    business_livestock_industry = config.business_livestock_industry 
    business_logistics_industry = config.business_logistics_industry 
    business_maintenance_industry = config.business_maintenance_industry 
    business_manufacturing_industry = config.business_manufacturing_industry 
    business_maritime_transport = config.business_maritime_transport 
    business_marketing = config.business_marketing 
    business_metals_mining_industry = config.business_metals_mining_industry 
    business_mining_industry = config.business_mining_industry 
    business_mining_precious_metals_industry = config.business_mining_precious_metals_industry 
    business_mlm = config.business_mlm 
    business_moving_industry = config.business_moving_industry 
    business_nonwovens_industry = config.business_nonwovens_industry 
    business_office_services = config.business_office_services 
    business_office_supplies = config.business_office_supplies 
    business_oil = config.business_oil 
    business_oil_industry = config.business_oil_industry 
    business_online_business = config.business_online_business 
    business_packaging_industry = config.business_packaging_industry 
    business_parking = config.business_parking 
    business_pharmaceuticals_industry = config.business_pharmaceuticals_industry 
    business_plastics_industry = config.business_plastics_industry 
    business_polymers_industry = config.business_polymers_industry 
    business_powerwasher = config.business_powerwasher 
    business_printing_industry = config.business_printing_industry 
    business_public_relations = config.business_public_relations 
    business_public_transportation = config.business_public_transportation 
    business_publishing_industry = config.business_publishing_industry 
    business_rail_transport = config.business_rail_transport 
    business_renewable_energy = config.business_renewable_energy 
    business_retail_equipment = config.business_retail_equipment 
    business_retail_industry = config.business_retail_industry 
    business_security = config.business_security 
    business_small_business = config.business_small_business 
    business_space_technology = config.business_space_technology 
    business_textiles_industry = config.business_textiles_industry 
    business_trade_industry = config.business_trade_industry 
    business_transportation_industry = config.business_transportation_industry 
    business_truckin_industry = config.business_truckin_industry 
    business_urban_transportation = config.business_urban_transportation 
    business_utilities_industry = config.business_utilities_industry 
    business_writing_services = config.business_writing_services 
    computer_bluetooth = config.computer_bluetooth 
    computers_apple_computer = config.computers_apple_computer 
    computers_audio_equipment = config.computers_audio_equipment 
    computers_business_software = config.computers_business_software 
    computers_c_language = config.computers_c_language 
    computers_cad_cam = config.computers_cad_cam 
    computers_camera = config.computers_camera 
    computers_camera_equipment = config.computers_camera_equipment 
    computers_car_electronics = config.computers_car_electronics 
    computers_computer_components = config.computers_computer_components 
    computers_computer_drives_storage = config.computers_computer_drives_storage 
    computers_computer_hacking = config.computers_computer_hacking 
    computers_computer_hardware = config.computers_computer_hardware 
    computers_computer_networking = config.computers_computer_networking 
    computers_computer_peripherals = config.computers_computer_peripherals 
    computers_computer_security = config.computers_computer_security 
    computers_computers = config.computers_computers 
    computers_computers_programming = config.computers_computers_programming 
    computers_computers_software = config.computers_computers_software 
    computers_consumer_electronics = config.computers_consumer_electronics 
    computers_data_management = config.computers_data_management 
    computers_dedicated_server = config.computers_dedicated_server 
    computers_desktop_computers = config.computers_desktop_computers 
    computers_drones = config.computers_drones 
    computers_electronic_components = config.computers_electronic_components 
    computers_electronics = config.computers_electronics 
    computers_elm_language = config.computers_elm_language 
    computers_enterprise_technology = config.computers_enterprise_technology 
    computers_game_consoles = config.computers_game_consoles 
    computers_go_language = config.computers_go_language 
    computers_gps_navigation = config.computers_gps_navigation 
    computers_hd = config.computers_hd 
    computers_hosting = config.computers_hosting 
    computers_image_software = config.computers_image_software 
    computers_internet_software = config.computers_internet_software 
    computers_it = config.computers_it 
    computers_java_language = config.computers_java_language 
    computers_javascript_language = config.computers_javascript_language 
    computers_laptops_computers = config.computers_laptops_computers 
    computers_linux = config.computers_linux 
    computers_mac = config.computers_mac 
    computers_mac = config.computers_mac 
    computers_marketing_software = config.computers_marketing_software 
    computers_microsoft = config.computers_microsoft 
    computers_microsoft_windows = config.computers_microsoft_windows 
    computers_multimedia_software = config.computers_multimedia_software 
    computers_music_software = config.computers_music_software 
    computers_network_monitoring = config.computers_network_monitoring 
    computers_networking_data_formats = config.computers_networking_data_formats 
    computers_operating_systems = config.computers_operating_systems 
    computers_pc = config.computers_pc 
    computers_php_language = config.computers_php_language 
    computers_power_supplies = config.computers_power_supplies 
    computers_proxies = config.computers_proxies 
    computers_python_language = config.computers_python_language 
    computers_rc_aircraft = config.computers_rc_aircraft 
    computers_ruby_language = config.computers_ruby_language 
    computers_rust_language = config.computers_rust_language 
    computers_scala_language = config.computers_scala_language 
    computers_sd_card = config.computers_sd_card 
    computers_seo_software = config.computers_seo_software 
    computers_software_cracking = config.computers_software_cracking 
    computers_software_device_drivers = config.computers_software_device_drivers 
    computers_ssd = config.computers_ssd 
    computers_surveillance_camera = config.computers_surveillance_camera 
    computers_swift_language = config.computers_swift_language 
    computers_torrent = config.computers_torrent 
    computers_torrent_software = config.computers_torrent_software 
    computers_utilities_software = config.computers_utilities_software 
    computers_video_equipment = config.computers_video_equipment 
    computers_video_software = config.computers_video_software 
    computers_vpns = config.computers_vpns 
    computers_wifi = config.computers_wifi 
    finance_accounting = config.finance_accounting 
    finance_auditing = config.finance_auditing 
    finance_auto_insurance = config.finance_auto_insurance 
    finance_banking = config.finance_banking 
    finance_billing = config.finance_billing 
    finance_boat_insurance = config.finance_boat_insurance 
    finance_car_finance = config.finance_car_finance 
    finance_commodities_trading = config.finance_commodities_trading 
    finance_credit = config.finance_credit 
    finance_credit_cards = config.finance_credit_cards 
    finance_credit_monitoring = config.finance_credit_monitoring 
    finance_credit_reporting = config.finance_credit_reporting 
    finance_cryptocurrencies = config.finance_cryptocurrencies 
    finance_cryptocurrencies_binance_coin = config.finance_cryptocurrencies_binance_coin 
    finance_cryptocurrencies_bitcoin = config.finance_cryptocurrencies_bitcoin 
    finance_cryptocurrencies_bitcoin_cash = config.finance_cryptocurrencies_bitcoin_cash 
    finance_cryptocurrencies_cardano = config.finance_cryptocurrencies_cardano 
    finance_cryptocurrencies_chainlink = config.finance_cryptocurrencies_chainlink 
    finance_cryptocurrencies_dash = config.finance_cryptocurrencies_dash 
    finance_cryptocurrencies_dogecoin = config.finance_cryptocurrencies_dogecoin 
    finance_cryptocurrencies_ethereum = config.finance_cryptocurrencies_ethereum 
    finance_cryptocurrencies_litecoin = config.finance_cryptocurrencies_litecoin 
    finance_cryptocurrencies_monero = config.finance_cryptocurrencies_monero 
    finance_cryptocurrencies_nxt = config.finance_cryptocurrencies_nxt 
    finance_cryptocurrencies_peercoin = config.finance_cryptocurrencies_peercoin 
    finance_cryptocurrencies_polkadot = config.finance_cryptocurrencies_polkadot 
    finance_cryptocurrencies_stellar = config.finance_cryptocurrencies_stellar 
    finance_cryptocurrencies_tether = config.finance_cryptocurrencies_tether 
    finance_finance = config.finance_finance 
    finance_finance_grants = config.finance_finance_grants 
    finance_finance_investing = config.finance_finance_investing 
    finance_finance_scholarships = config.finance_finance_scholarships 
    finance_financial_aid = config.finance_financial_aid 
    finance_financial_planning = config.finance_financial_planning 
    finance_futures_trading = config.finance_futures_trading 
    finance_health_insurance = config.finance_health_insurance 
    finance_home_insurance = config.finance_home_insurance 
    finance_insurance = config.finance_insurance 
    finance_invest_home = config.finance_invest_home 
    finance_investing_bonds = config.finance_investing_bonds 
    finance_investing_currencies = config.finance_investing_currencies 
    finance_investing_gold = config.finance_investing_gold 
    finance_investing_oil = config.finance_investing_oil 
    finance_investing_precious_metals = config.finance_investing_precious_metals 
    finance_investing_silver = config.finance_investing_silver 
    finance_investing_stocks = config.finance_investing_stocks 
    finance_invoicing = config.finance_invoicing 
    finance_lending = config.finance_lending 
    finance_life_insurance = config.finance_life_insurance 
    finance_loans = config.finance_loans 
    finance_retirement_pension = config.finance_retirement_pension 
    finance_retirement_planning = config.finance_retirement_planning 
    finance_stocks = config.finance_stocks 
    finance_tax_preparation = config.finance_tax_preparation 
    food_baked_goods = config.food_baked_goods 
    food_bbq_cooking = config.food_bbq_cooking 
    food_bbq_recipes = config.food_bbq_recipes 
    food_beer = config.food_beer 
    food_beverage_drinks = config.food_beverage_drinks 
    food_breakfast_foods = config.food_breakfast_foods 
    food_candy = config.food_candy 
    food_coffee = config.food_coffee 
    food_cooking_recipes = config.food_cooking_recipes 
    food_dessert_recipes = config.food_dessert_recipes 
    food_drink = config.food_drink 
    food_fast_food = config.food_fast_food 
    food_food = config.food_food 
    food_food_cooking = config.food_food_cooking 
    food_food_grains = config.food_food_grains 
    food_grill_cooking = config.food_grill_cooking 
    food_grill_recipes = config.food_grill_recipes 
    food_grocery_retailers = config.food_grocery_retailers 
    food_grocery_stores = config.food_grocery_stores 
    food_juice_beverages = config.food_juice_beverages 
    food_liquor = config.food_liquor 
    food_meat_foods = config.food_meat_foods 
    food_pasta = config.food_pasta 
    food_pizzerias = config.food_pizzerias 
    food_restaurant_reservations = config.food_restaurant_reservations 
    food_restaurant_reviews = config.food_restaurant_reviews 
    food_restaurants = config.food_restaurants 
    food_seafood = config.food_seafood 
    food_snack_foods = config.food_snack_foods 
    food_soft_drinks = config.food_soft_drinks 
    food_soup_recipes = config.food_soup_recipes 
    food_spirit_alcohol = config.food_spirit_alcohol 
    food_stew_recipes = config.food_stew_recipes 
    food_sweets = config.food_sweets 
    food_tea = config.food_tea 
    food_wine = config.food_wine 
    games_arcade_games = config.games_arcade_games 
    games_billiards_games = config.games_billiards_games 
    games_blackjack_games = config.games_blackjack_games 
    games_board_games = config.games_board_games 
    games_brainteasers = config.games_brainteasers 
    games_card_games = config.games_card_games 
    games_casino_games = config.games_casino_games 
    games_casual_video_games = config.games_casual_video_games 
    games_checkers_games = config.games_checkers_games 
    games_chess_game = config.games_chess_game 
    games_collectible_card_games = config.games_collectible_card_games 
    games_collectible_cards = config.games_collectible_cards 
    games_coloring = config.games_coloring 
    games_drawing = config.games_drawing 
    games_dress_up_games = config.games_dress_up_games 
    games_family_drawing_coloring = config.games_family_drawing_coloring 
    games_family_dress_up_games = config.games_family_dress_up_games 
    games_family_games = config.games_family_games 
    games_gambling = config.games_gambling 
    games_games = config.games_games 
    games_lottery = config.games_lottery 
    games_online_massively_multiplayer_games = config.games_online_massively_multiplayer_games 
    games_poker_games = config.games_poker_games 
    games_puzzles = config.games_puzzles 
    games_roleplaying_games = config.games_roleplaying_games 
    games_strategy_games = config.games_strategy_games 
    games_table_games = config.games_table_games 
    games_video_dance_games = config.games_video_dance_games 
    games_video_driving_games = config.games_video_driving_games 
    games_video_fighting_games = config.games_video_fighting_games 
    games_video_flying_games = config.games_video_flying_games 
    games_video_game_emulation = config.games_video_game_emulation 
    games_video_games = config.games_video_games 
    games_video_puzzle_games = config.games_video_puzzle_games 
    games_video_racing_games = config.games_video_racing_games 
    games_video_sandbox_games = config.games_video_sandbox_games 
    games_video_shooter_games = config.games_video_shooter_games 
    games_video_simulation_games = config.games_video_simulation_games 
    games_video_sports_games = config.games_video_sports_games 
    games_video_strategy_games = config.games_video_strategy_games 
    games_video_war_games = config.games_video_war_games 
    games_video_word_games = config.games_video_word_games 
    games_war_games = config.games_war_games 
    games_word_games = config.games_word_games 
    general_alternative_energy = config.general_alternative_energy 
    general_conservation = config.general_conservation 
    general_disorder = config.general_disorder 
    general_energy = config.general_energy 
    general_masonry = config.general_masonry 
    general_repair = config.general_repair 
    general_utilities = config.general_utilities 
    health_aids = config.health_aids 
    health_alcohol_testing = config.health_alcohol_testing 
    health_alcohol_treatment = config.health_alcohol_treatment 
    health_allergies = config.health_allergies 
    health_anxiety = config.health_anxiety 
    health_arthritis = config.health_arthritis 
    health_assisted_living = config.health_assisted_living 
    health_cancer = config.health_cancer 
    health_conditions_ear = config.health_conditions_ear 
    health_conditions_ear_nose_throat = config.health_conditions_ear_nose_throat 
    health_conditions_ethroat = config.health_conditions_ethroat 
    health_conditions_nose = config.health_conditions_nose 
    health_contacts = config.health_contacts 
    health_covid = config.health_covid 
    health_dental_care = config.health_dental_care 
    health_depression = config.health_depression 
    health_diabetes = config.health_diabetes 
    health_diets = config.health_diets 
    health_disabilities = config.health_disabilities 
    health_doctors_offices = config.health_doctors_offices 
    health_drug_testing = config.health_drug_testing 
    health_drug_treatment = config.health_drug_treatment 
    health_eating_disorders = config.health_eating_disorders 
    health_endocrine_conditions = config.health_endocrine_conditions 
    health_eyeglasses = config.health_eyeglasses 
    health_genetic_disorders = config.health_genetic_disorders 
    health_health = config.health_health 
    health_health_aging = config.health_health_aging 
    health_health_conditions = config.health_health_conditions 
    health_health_pharmacy = config.health_health_pharmacy 
    health_health_quit_smoking = config.health_health_quit_smoking 
    health_health_records = config.health_health_records 
    health_heart_conditions = config.health_heart_conditions 
    health_hiv = config.health_hiv 
    health_homeopathy = config.health_homeopathy 
    health_hospitals = config.health_hospitals 
    health_hypertension = config.health_hypertension 
    health_immune_system = config.health_immune_system 
    health_infectious_diseases = config.health_infectious_diseases 
    health_medical_devices = config.health_medical_devices 
    health_medical_equipment = config.health_medical_equipment 
    health_medical_facilities = config.health_medical_facilities 
    health_medical_procedures = config.health_medical_procedures 
    health_medical_research = config.health_medical_research 
    health_medical_services = config.health_medical_services 
    health_medical_training = config.health_medical_training 
    health_medications = config.health_medications 
    health_meditation = config.health_meditation 
    health_men_health = config.health_men_health 
    health_mental_health = config.health_mental_health 
    health_mental_therapy = config.health_mental_therapy 
    health_neurological_conditions = config.health_neurological_conditions 
    health_nursing_service = config.health_nursing_service 
    health_nutrition = config.health_nutrition 
    health_nutrition_supplements = config.health_nutrition_supplements 
    health_obesity = config.health_obesity 
    health_occupational_health = config.health_occupational_health 
    health_occupational_safety = config.health_occupational_safety 
    health_oral_care = config.health_oral_care 
    health_pain_management = config.health_pain_management 
    health_physical_therapy = config.health_physical_therapy 
    health_public_health = config.health_public_health 
    health_reproductive_health = config.health_reproductive_health 
    health_respiratory_conditions = config.health_respiratory_conditions 
    health_restricted_diets = config.health_restricted_diets 
    health_skin_conditions = config.health_skin_conditions 
    health_sleep_disorders = config.health_sleep_disorders 
    health_special_diets = config.health_special_diets 
    health_steroids_abuse = config.health_steroids_abuse 
    health_stress = config.health_stress 
    health_substance_abuse = config.health_substance_abuse 
    health_therapy = config.health_therapy 
    health_trauma = config.health_trauma 
    health_treatment_centers = config.health_treatment_centers 
    health_vision_care = config.health_vision_care 
    health_vitamins_supplements = config.health_vitamins_supplements 
    health_women_health = config.health_women_health 
    hobbies_arts_crafts = config.hobbies_arts_crafts 
    hobbies_boating = config.hobbies_boating 
    hobbies_camping = config.hobbies_camping 
    hobbies_clubs = config.hobbies_clubs 
    hobbies_contests = config.hobbies_contests 
    hobbies_crafts = config.hobbies_crafts 
    hobbies_fiber_crafts = config.hobbies_fiber_crafts 
    hobbies_fishing = config.hobbies_fishing 
    hobbies_hiking = config.hobbies_hiking 
    hobbies_hobbies = config.hobbies_hobbies 
    hobbies_leisure = config.hobbies_leisure 
    hobbies_merit_prizes = config.hobbies_merit_prizes 
    hobbies_model_railroads = config.hobbies_model_railroads 
    hobbies_model_trains = config.hobbies_model_trains 
    hobbies_modeling = config.hobbies_modeling 
    hobbies_organizations = config.hobbies_organizations 
    hobbies_outdoors = config.hobbies_outdoors 
    hobbies_paintball = config.hobbies_paintball 
    hobbies_radio_control = config.hobbies_radio_control 
    hobbies_seasonal_events = config.hobbies_seasonal_events 
    hobbies_special_holidays = config.hobbies_special_holidays 
    hobbies_special_occasions = config.hobbies_special_occasions 
    hobbies_surfing = config.hobbies_surfing 
    hobbies_swimming = config.hobbies_swimming 
    hobbies_textile_crafts = config.hobbies_textile_crafts 
    hobbies_weddings = config.hobbies_weddings 
    hobbies_youth_clubs = config.hobbies_youth_clubs 
    hobbies_youth_organizations = config.hobbies_youth_organizations 
    hobbies_youth_resources = config.hobbies_youth_resources 
    home_bed = config.home_bed 
    home_curtains_treatments = config.home_curtains_treatments 
    home_dining_furniture = config.home_dining_furniture 
    home_domestic_services = config.home_domestic_services 
    home_foundation = config.home_foundation 
    home_garden = config.home_garden 
    home_garden_pest_control = config.home_garden_pest_control 
    home_home = config.home_home 
    home_home_appliances = config.home_home_appliances 
    home_home_carpets = config.home_home_carpets 
    home_home_climate_control = config.home_home_climate_control 
    home_home_cookware = config.home_home_cookware 
    home_home_curtains = config.home_home_curtains 
    home_home_decoration = config.home_home_decoration 
    home_home_dining_room = config.home_home_dining_room 
    home_home_diningware = config.home_home_diningware 
    home_home_dryers = config.home_home_dryers 
    home_home_fireplaces = config.home_home_fireplaces 
    home_home_flooring = config.home_home_flooring 
    home_home_furnishings = config.home_home_furnishings 
    home_home_furniture = config.home_home_furniture 
    home_home_garden = config.home_home_garden 
    home_home_garden_bed_bath_bathroom = config.home_home_garden_bed_bath_bathroom 
    home_home_garden_domestic_services_cleaning_services = config.home_home_garden_domestic_services_cleaning_services 
    home_home_garden_laundry = config.home_home_garden_laundry 
    home_home_garden_yard_patio_lawn_mowers = config.home_home_garden_yard_patio_lawn_mowers 
    home_home_gardening = config.home_home_gardening 
    home_home_gym = config.home_home_gym 
    home_home_hvac = config.home_home_hvac 
    home_home_improvement = config.home_home_improvement 
    home_home_improvement_doors = config.home_home_improvement_doors 
    home_home_improvement_flooring = config.home_home_improvement_flooring 
    home_home_improvement_plumbing = config.home_home_improvement_plumbing 
    home_home_improvement_windows = config.home_home_improvement_windows 
    home_home_kitchen = config.home_home_kitchen 
    home_home_landscaping = config.home_home_landscaping 
    home_home_lighting = config.home_home_lighting 
    home_home_nursery = config.home_home_nursery 
    home_home_pest_control = config.home_home_pest_control 
    home_home_playroom = config.home_home_playroom 
    home_home_plumbing = config.home_home_plumbing 
    home_home_rugs = config.home_home_rugs 
    home_home_safety = config.home_home_safety 
    home_home_saunas = config.home_home_saunas 
    home_home_security = config.home_home_security 
    home_home_shelving = config.home_home_shelving 
    home_home_spas = config.home_home_spas 
    home_home_storage = config.home_home_storage 
    home_home_stoves = config.home_home_stoves 
    home_home_swimming_pools = config.home_home_swimming_pools 
    home_home_washers = config.home_home_washers 
    home_home_windows = config.home_home_windows 
    home_house_finishing = config.home_house_finishing 
    home_house_painting = config.home_house_painting 
    home_interior_decor = config.home_interior_decor 
    home_lamps = config.home_lamps 
    home_living_room_furniture = config.home_living_room_furniture 
    home_major_kitchen_appliances = config.home_major_kitchen_appliances 
    home_patio = config.home_patio 
    home_patio_funiture = config.home_patio_funiture 
    home_pest_control = config.home_pest_control 
    home_power_tools = config.home_power_tools 
    home_small_kitchen_appliances = config.home_small_kitchen_appliances 
    home_window_treatments = config.home_window_treatments 
    home_yard = config.home_yard 
    internet_affiliate_programs = config.internet_affiliate_programs 
    internet_cable_providers = config.internet_cable_providers 
    internet_cable_satellite_providers = config.internet_cable_satellite_providers 
    internet_communication_equipment = config.internet_communication_equipment 
    internet_email = config.internet_email 
    internet_instant_messaging = config.internet_instant_messaging 
    internet_internet = config.internet_internet 
    internet_internet_service_providers = config.internet_internet_service_providers 
    internet_internet_services = config.internet_internet_services 
    internet_mobile_accessories = config.internet_mobile_accessories 
    internet_mobile_add_ons = config.internet_mobile_add_ons 
    internet_mobile_apps = config.internet_mobile_apps 
    internet_mobile_communications = config.internet_mobile_communications 
    internet_mobile_phones = config.internet_mobile_phones 
    internet_opera_browser = config.internet_opera_browser 
    internet_radio_equipment = config.internet_radio_equipment 
    internet_search = config.internet_search 
    internet_seo = config.internet_seo 
    internet_telecom = config.internet_telecom 
    internet_telecom_equipment = config.internet_telecom_equipment 
    internet_text_messaging = config.internet_text_messaging 
    internet_video_chat = config.internet_video_chat 
    internet_voice_chat = config.internet_voice_chat 
    internet_web_design = config.internet_web_design 
    internet_web_development = config.internet_web_development 
    internet_web_services = config.internet_web_services 
    internet_website = config.internet_website 
    internet_wireless = config.internet_wireless 
    internet_wireless_accessories = config.internet_wireless_accessories 
    jobs_career_planning = config.jobs_career_planning 
    jobs_career_resources = config.jobs_career_resources 
    jobs_classroom_resources = config.jobs_classroom_resources 
    jobs_colleges = config.jobs_colleges 
    jobs_continuing_education = config.jobs_continuing_education 
    jobs_distance_learning = config.jobs_distance_learning 
    jobs_homeschooling = config.jobs_homeschooling 
    jobs_job_education = config.jobs_job_education 
    jobs_job_listings = config.jobs_job_listings 
    jobs_jobs = config.jobs_jobs 
    jobs_jobs_planning = config.jobs_jobs_planning 
    jobs_jobs_portfolios = config.jobs_jobs_portfolios 
    jobs_jobs_resources = config.jobs_jobs_resources 
    jobs_jobs_resumes = config.jobs_jobs_resumes 
    jobs_k_12 = config.jobs_k_12 
    jobs_online_courses = config.jobs_online_courses 
    jobs_primary_schooling_k_12 = config.jobs_primary_schooling_k_12 
    jobs_remote_education = config.jobs_remote_education 
    jobs_secondary_schooling = config.jobs_secondary_schooling 
    jobs_standardized_admissions_tests = config.jobs_standardized_admissions_tests 
    jobs_teaching_jobs = config.jobs_teaching_jobs 
    jobs_teaching_resources = config.jobs_teaching_resources 
    jobs_training_certification = config.jobs_training_certification 
    jobs_universities = config.jobs_universities 
    jobs_vocational_education = config.jobs_vocational_education 
    law_bankruptcy = config.law_bankruptcy 
    law_crime = config.law_crime 
    law_dui = config.law_dui 
    law_emergency_services = config.law_emergency_services 
    law_government = config.law_government 
    law_government_laws = config.law_government_laws 
    law_government_security = config.law_government_security 
    law_immigration_law = config.law_immigration_law 
    law_incarceration = config.law_incarceration 
    law_judiciary = config.law_judiciary 
    law_justice = config.law_justice 
    law_law = config.law_law 
    law_law_courts = config.law_law_courts 
    law_law_enforcement = config.law_law_enforcement 
    law_law_military = config.law_law_military 
    law_lawyers = config.law_lawyers 
    law_legal = config.law_legal 
    law_legal_education = config.law_legal_education 
    law_legal_services = config.law_legal_services 
    law_public_safety = config.law_public_safety 
    law_public_safety_services = config.law_public_safety_services 
    law_security_products = config.law_security_products 
    law_security_servicess = config.law_security_servicess 
    law_social_services = config.law_social_services 
    law_visa_law = config.law_visa_law 
    news_business_news = config.news_business_news 
    news_company_news = config.news_company_news 
    news_disasters = config.news_disasters 
    news_economics_news = config.news_economics_news 
    news_financial_news = config.news_financial_news 
    news_gossip = config.news_gossip 
    news_health_news = config.news_health_news 
    news_industry_news = config.news_industry_news 
    news_investigation_news = config.news_investigation_news 
    news_markets_news = config.news_markets_news 
    news_news = config.news_news 
    news_news_politics = config.news_news_politics 
    news_news_politics_communism = config.news_news_politics_communism 
    news_news_politics_democrats = config.news_news_politics_democrats 
    news_news_politics_fascism = config.news_news_politics_fascism 
    news_news_politics_green_party = config.news_news_politics_green_party 
    news_news_politics_libertarian = config.news_news_politics_libertarian 
    news_news_politics_republicans = config.news_news_politics_republicans 
    news_news_sports_news = config.news_news_sports_news 
    news_news_weather = config.news_news_weather 
    news_scandals = config.news_scandals 
    news_tabloid = config.news_tabloid 
    online_animated_gifs = config.online_animated_gifs 
    online_blogging = config.online_blogging 
    online_communities = config.online_communities 
    online_communities_social_networks = config.online_communities_social_networks 
    online_communities_virtual_worlds = config.online_communities_virtual_worlds 
    online_design_skins = config.online_design_skins 
    online_design_themes = config.online_design_themes 
    online_design_wallpapers = config.online_design_wallpapers 
    online_file_hosting = config.online_file_hosting 
    online_file_sharing = config.online_file_sharing 
    online_free_online = config.online_free_online 
    online_online_dating = config.online_online_dating 
    online_online_matrimonial = config.online_online_matrimonial 
    online_online_personals = config.online_online_personals 
    online_photo_rating = config.online_photo_rating 
    online_photo_sharing = config.online_photo_sharing 
    online_social_network_apps = config.online_social_network_apps 
    online_social_networks = config.online_social_networks 
    online_video_sharing = config.online_video_sharing 
    online_virtual_worlds = config.online_virtual_worlds 
    real_estate_commercial_properties = config.real_estate_commercial_properties 
    real_estate_foreclosed_properties = config.real_estate_foreclosed_properties 
    real_estate_listings_rentals = config.real_estate_listings_rentals 
    real_estate_listings_residential = config.real_estate_listings_residential 
    real_estate_real_estate = config.real_estate_real_estate 
    real_estate_real_estate_land = config.real_estate_real_estate_land 
    real_estate_real_estate_listings = config.real_estate_real_estate_listings 
    real_estate_real_estate_lots = config.real_estate_real_estate_lots 
    real_estate_real_estate_services = config.real_estate_real_estate_services 
    real_estate_residential_sales = config.real_estate_residential_sales 
    real_estate_timeshares = config.real_estate_timeshares 
    real_estate_vacation_properties = config.real_estate_vacation_properties 
    reference_arabic_resources = config.reference_arabic_resources 
    reference_autobiographies = config.reference_autobiographies 
    reference_biographies = config.reference_biographies 
    reference_business_listings = config.reference_business_listings 
    reference_calculators = config.reference_calculators 
    reference_calendars = config.reference_calendars 
    reference_chinese_resources = config.reference_chinese_resources 
    reference_dictionaries = config.reference_dictionaries 
    reference_directories = config.reference_directories 
    reference_encyclopedias = config.reference_encyclopedias 
    reference_english_resources = config.reference_english_resources 
    reference_folklore = config.reference_folklore 
    reference_foreign_language_resources = config.reference_foreign_language_resources 
    reference_french_resources = config.reference_french_resources 
    reference_geographic_reference = config.reference_geographic_reference 
    reference_german_resources = config.reference_german_resources 
    reference_hindi_resources = config.reference_hindi_resources 
    reference_language_resources = config.reference_language_resources 
    reference_libraries = config.reference_libraries 
    reference_maps = config.reference_maps 
    reference_museums = config.reference_museums 
    reference_myths = config.reference_myths 
    reference_personal_listings = config.reference_personal_listings 
    reference_public_records = config.reference_public_records 
    reference_quotations = config.reference_quotations 
    reference_reference = config.reference_reference 
    reference_reference_forms = config.reference_reference_forms 
    reference_reference_general_reference = config.reference_reference_general_reference 
    reference_reference_guides = config.reference_reference_guides 
    reference_reference_history = config.reference_reference_history 
    reference_reference_humanities = config.reference_reference_humanities 
    reference_reference_philosophy = config.reference_reference_philosophy 
    reference_reference_time = config.reference_reference_time 
    reference_reference_tools = config.reference_reference_tools 
    reference_resource = config.reference_resource 
    reference_russian_resources = config.reference_russian_resources 
    reference_spanish_resources = config.reference_spanish_resources 
    reference_templates = config.reference_templates 
    science_astronomy = config.science_astronomy 
    science_atmospheric_science = config.science_atmospheric_science 
    science_biology = config.science_biology 
    science_chemistry = config.science_chemistry 
    science_climate_change = config.science_climate_change 
    science_computer_science = config.science_computer_science 
    science_cosmos = config.science_cosmos 
    science_dynamics = config.science_dynamics 
    science_earth_science = config.science_earth_science 
    science_ecology = config.science_ecology 
    science_engineering = config.science_engineering 
    science_geology = config.science_geology 
    science_global_warming = config.science_global_warming 
    science_mathematics = config.science_mathematics 
    science_nasa = config.science_nasa 
    science_neuroscience = config.science_neuroscience 
    science_physics = config.science_physics 
    science_robotics = config.science_robotics 
    science_science = config.science_science 
    science_science_earth_sciences = config.science_science_earth_sciences 
    science_science_environment = config.science_science_environment 
    science_scientific_institutions = config.science_scientific_institutions 
    science_statistics = config.science_statistics 
    science_technology = config.science_technology 
    sensitive_subjects = config.sensitive_subjects 
    shopping = config.shopping 
    shopping_building_toys = config.shopping_building_toys 
    shopping_cards_greetings = config.shopping_cards_greetings 
    shopping_classifieds = config.shopping_classifieds 
    shopping_classifieds_buying = config.shopping_classifieds_buying 
    shopping_classifieds_selling = config.shopping_classifieds_selling 
    shopping_consumer_advocacy = config.shopping_consumer_advocacy 
    shopping_consumer_protection = config.shopping_consumer_protection 
    shopping_coupons = config.shopping_coupons 
    shopping_department_stores = config.shopping_department_stores 
    shopping_discounts = config.shopping_discounts 
    shopping_dolls = config.shopping_dolls 
    shopping_dolls_accessories = config.shopping_dolls_accessories 
    shopping_electronic_cigarettes = config.shopping_electronic_cigarettes 
    shopping_entertainment_media = config.shopping_entertainment_media 
    shopping_gifts = config.shopping_gifts 
    shopping_luxury_goods = config.shopping_luxury_goods 
    shopping_malls = config.shopping_malls 
    shopping_marijuana = config.shopping_marijuana 
    shopping_marijuana_accessories = config.shopping_marijuana_accessories 
    shopping_media_rentals = config.shopping_media_rentals 
    shopping_offers = config.shopping_offers 
    shopping_online_shopping = config.shopping_online_shopping 
    shopping_online_stores = config.shopping_online_stores 
    shopping_outdoor_backpacks = config.shopping_outdoor_backpacks 
    shopping_outdoor_hiking_boots = config.shopping_outdoor_hiking_boots 
    shopping_outdoor_tents = config.shopping_outdoor_tents 
    shopping_photo_services = config.shopping_photo_services 
    shopping_price_comparisons = config.shopping_price_comparisons 
    shopping_ride_on_toys = config.shopping_ride_on_toys 
    shopping_ride_on_wagons = config.shopping_ride_on_wagons 
    shopping_sales = config.shopping_sales 
    shopping_shopping_antiques = config.shopping_shopping_antiques 
    shopping_shopping_apparel = config.shopping_shopping_apparel 
    shopping_shopping_athletic_apparel = config.shopping_shopping_athletic_apparel 
    shopping_shopping_auctions = config.shopping_shopping_auctions 
    shopping_shopping_casual_apparel = config.shopping_shopping_casual_apparel 
    shopping_shopping_children_clothing = config.shopping_shopping_children_clothing 
    shopping_shopping_children_shopping = config.shopping_shopping_children_shopping 
    shopping_shopping_clothing_accessories = config.shopping_shopping_clothing_accessories 
    shopping_shopping_collectibles = config.shopping_shopping_collectibles 
    shopping_shopping_consumer_resources = config.shopping_shopping_consumer_resources 
    shopping_shopping_costumes = config.shopping_shopping_costumes 
    shopping_shopping_eyewear = config.shopping_shopping_eyewear 
    shopping_shopping_flowers = config.shopping_shopping_flowers 
    shopping_shopping_footwear = config.shopping_shopping_footwear 
    shopping_shopping_formal_wear = config.shopping_shopping_formal_wear 
    shopping_shopping_gifts = config.shopping_shopping_gifts 
    shopping_shopping_headwear = config.shopping_shopping_headwear 
    shopping_shopping_media = config.shopping_shopping_media 
    shopping_shopping_men = config.shopping_shopping_men 
    shopping_shopping_men_clothing = config.shopping_shopping_men_clothing 
    shopping_shopping_men_shoe = config.shopping_shopping_men_shoe 
    shopping_shopping_men_suit = config.shopping_shopping_men_suit 
    shopping_shopping_men_tie = config.shopping_shopping_men_tie 
    shopping_shopping_special = config.shopping_shopping_special 
    shopping_shopping_swimwear = config.shopping_shopping_swimwear 
    shopping_shopping_toys_die_cast_toy_vehicles = config.shopping_shopping_toys_die_cast_toy_vehicles 
    shopping_shopping_undergarments = config.shopping_shopping_undergarments 
    shopping_shopping_women = config.shopping_shopping_women 
    shopping_shopping_women_clothing = config.shopping_shopping_women_clothing 
    shopping_smokeless_tobacco = config.shopping_smokeless_tobacco 
    shopping_smoking_accessories = config.shopping_smoking_accessories 
    shopping_sports_equipment = config.shopping_sports_equipment 
    shopping_stuffed_toys = config.shopping_stuffed_toys 
    shopping_tobacco = config.shopping_tobacco 
    shopping_tobacco_accessories = config.shopping_tobacco_accessories 
    shopping_tobacco_cigarettes = config.shopping_tobacco_cigarettes 
    shopping_tobacco_cigars = config.shopping_tobacco_cigars 
    shopping_tobacco_pipe = config.shopping_tobacco_pipe 
    shopping_toys = config.shopping_toys 
    shopping_vaping = config.shopping_vaping 
    shopping_video_services = config.shopping_video_services 
    society_advocacy_labor = config.society_advocacy_labor 
    society_beliefs = config.society_beliefs 
    society_bisexual = config.society_bisexual 
    society_charity = config.society_charity 
    society_children = config.society_children 
    society_dating = config.society_dating 
    society_discrimination_advocacy = config.society_discrimination_advocacy 
    society_economics = config.society_economics 
    society_environmental_advocacy = config.society_environmental_advocacy 
    society_family_relationship_aunt = config.society_family_relationship_aunt 
    society_family_relationship_boyfriend = config.society_family_relationship_boyfriend 
    society_family_relationship_brother = config.society_family_relationship_brother 
    society_family_relationship_father = config.society_family_relationship_father 
    society_family_relationship_girlfriend = config.society_family_relationship_girlfriend 
    society_family_relationship_grandchild = config.society_family_relationship_grandchild 
    society_family_relationship_grandparent = config.society_family_relationship_grandparent 
    society_family_relationship_husband = config.society_family_relationship_husband 
    society_family_relationship_mother = config.society_family_relationship_mother 
    society_family_relationship_parent = config.society_family_relationship_parent 
    society_family_relationship_sister = config.society_family_relationship_sister 
    society_family_relationship_uncle = config.society_family_relationship_uncle 
    society_family_relationship_wife = config.society_family_relationship_wife 
    society_family_relationships = config.society_family_relationships 
    society_family_relationships_children = config.society_family_relationships_children 
    society_gay = config.society_gay 
    society_guns = config.society_guns 
    society_human_liberties = config.society_human_liberties 
    society_human_rights = config.society_human_rights 
    society_hunger = config.society_hunger 
    society_identity_advocacy = config.society_identity_advocacy 
    society_identity_politics = config.society_identity_politics 
    society_kids_teens_children_interests = config.society_kids_teens_children_interests 
    society_kids_teens_teen_interests = config.society_kids_teens_teen_interests 
    society_labor_issues = config.society_labor_issues 
    society_lesbian = config.society_lesbian 
    society_lgbtq = config.society_lgbtq 
    society_mentor = config.society_mentor 
    society_people = config.society_people 
    society_philanthropy = config.society_philanthropy 
    society_political_science = config.society_political_science 
    society_poverty = config.society_poverty 
    society_privacy = config.society_privacy 
    society_queer = config.society_queer 
    society_relations_advocacy = config.society_relations_advocacy 
    society_relationship_student = config.society_relationship_student 
    society_relationship_teacher = config.society_relationship_teacher 
    society_relationships_marriage = config.society_relationships_marriage 
    society_religion = config.society_religion 
    society_responsibility = config.society_responsibility 
    society_retirement = config.society_retirement 
    society_self_defense = config.society_self_defense 
    society_self_improvement = config.society_self_improvement 
    society_social_advocacy = config.society_social_advocacy 
    society_social_issues = config.society_social_issues 
    society_social_justice = config.society_social_justice 
    society_social_sciences = config.society_social_sciences 
    society_social_sciences_psychology = config.society_social_sciences_psychology 
    society_society = config.society_society 
    society_straight_sexuality = config.society_straight_sexuality 
    society_subcultures_niche_interests = config.society_subcultures_niche_interests 
    society_teens = config.society_teens 
    society_transgender = config.society_transgender 
    society_troubled_relationships = config.society_troubled_relationships 
    society_war = config.society_war 
    sports_american_football = config.sports_american_football 
    sports_american_soccer = config.sports_american_soccer 
    sports_animal_sports = config.sports_animal_sports 
    sports_australian_football = config.sports_australian_football 
    sports_auto_racing = config.sports_auto_racing 
    sports_baseball = config.sports_baseball 
    sports_basketball = config.sports_basketball 
    sports_boat_racing = config.sports_boat_racing 
    sports_boxing = config.sports_boxing 
    sports_coaching = config.sports_coaching 
    sports_coaching_coaching = config.sports_coaching_coaching 
    sports_coaching_training = config.sports_coaching_training 
    sports_college_baseball = config.sports_college_baseball 
    sports_college_basketball = config.sports_college_basketball 
    sports_college_football = config.sports_college_football 
    sports_college_sports = config.sports_college_sports 
    sports_combat_sports = config.sports_combat_sports 
    sports_cricket = config.sports_cricket 
    sports_cycling = config.sports_cycling 
    sports_diving = config.sports_diving 
    sports_dog_racing = config.sports_dog_racing 
    sports_drag_racing = config.sports_drag_racing 
    sports_extreme_sports = config.sports_extreme_sports 
    sports_fantasy_sports = config.sports_fantasy_sports 
    sports_football = config.sports_football 
    sports_golf = config.sports_golf 
    sports_gymnastics = config.sports_gymnastics 
    sports_hockey = config.sports_hockey 
    sports_horse_racing = config.sports_horse_racing 
    sports_ice_skating = config.sports_ice_skating 
    sports_international_sports = config.sports_international_sports 
    sports_martial_arts = config.sports_martial_arts 
    sports_mlb_american_baseball = config.sports_mlb_american_baseball 
    sports_mls_american_soccer = config.sports_mls_american_soccer 
    sports_motocycle_racing = config.sports_motocycle_racing 
    sports_motor_sports = config.sports_motor_sports 
    sports_nba_american_basketball = config.sports_nba_american_basketball 
    sports_nfl_american_football = config.sports_nfl_american_football 
    sports_nhl_american_hockey = config.sports_nhl_american_hockey 
    sports_olympics = config.sports_olympics 
    sports_personal_sports = config.sports_personal_sports 
    sports_pga_american_golf = config.sports_pga_american_golf 
    sports_pro_baseball = config.sports_pro_baseball 
    sports_pro_basketball = config.sports_pro_basketball 
    sports_pro_cycling = config.sports_pro_cycling 
    sports_pro_golf = config.sports_pro_golf 
    sports_pro_gymnastics = config.sports_pro_gymnastics 
    sports_pro_ice_skating = config.sports_pro_ice_skating 
    sports_pro_racquet_sports = config.sports_pro_racquet_sports 
    sports_pro_skate_sports = config.sports_pro_skate_sports 
    sports_pro_skateboarding = config.sports_pro_skateboarding 
    sports_pro_skating = config.sports_pro_skating 
    sports_pro_tennis = config.sports_pro_tennis 
    sports_racquet_sports = config.sports_racquet_sports 
    sports_racquetball = config.sports_racquetball 
    sports_rugby = config.sports_rugby 
    sports_scuba = config.sports_scuba 
    sports_skate_sports = config.sports_skate_sports 
    sports_skateboarding = config.sports_skateboarding 
    sports_skating = config.sports_skating 
    sports_skiing = config.sports_skiing 
    sports_snowboarding = config.sports_snowboarding 
    sports_soccer = config.sports_soccer 
    sports_sporting_goods = config.sports_sporting_goods 
    sports_sports = config.sports_sports 
    sports_sports_memorabilia = config.sports_sports_memorabilia 
    sports_sports_surfing = config.sports_sports_surfing 
    sports_sports_swimming = config.sports_sports_swimming 
    sports_sports_team = config.sports_sports_team 
    sports_sports_water_sports = config.sports_sports_water_sports 
    sports_street_racing = config.sports_street_racing 
    sports_summer_sports = config.sports_summer_sports 
    sports_team_baseball = config.sports_team_baseball 
    sports_team_basketball = config.sports_team_basketball 
    sports_team_cheerleading = config.sports_team_cheerleading 
    sports_team_cricket = config.sports_team_cricket 
    sports_team_hockey = config.sports_team_hockey 
    sports_team_rugby = config.sports_team_rugby 
    sports_team_soccer = config.sports_team_soccer 
    sports_team_volleyball = config.sports_team_volleyball 
    sports_tennis = config.sports_tennis 
    sports_track_field = config.sports_track_field 
    sports_ufc = config.sports_ufc 
    sports_volleyball = config.sports_volleyball 
    sports_winter_sports = config.sports_winter_sports 
    sports_winter_sports_equipment = config.sports_winter_sports_equipment 
    sports_wrestling = config.sports_wrestling 
    travel_accommodations = config.travel_accommodations 
    travel_airport_parking = config.travel_airport_parking 
    travel_airport_transportation = config.travel_airport_transportation 
    travel_car_rental = config.travel_car_rental 
    travel_charters = config.travel_charters 
    travel_cruises = config.travel_cruises 
    travel_destinations_beaches = config.travel_destinations_beaches 
    travel_destinations_islands = config.travel_destinations_islands 
    travel_hotels = config.travel_hotels 
    travel_motels = config.travel_motels 
    travel_mountain_resorts = config.travel_mountain_resorts 
    travel_national_parks = config.travel_national_parks 
    travel_nature_preserves = config.travel_nature_preserves 
    travel_parks = config.travel_parks 
    travel_regional_parks = config.travel_regional_parks 
    travel_short_term_stays = config.travel_short_term_stays 
    travel_ski_resorts = config.travel_ski_resorts 
    travel_specialty_travel = config.travel_specialty_travel 
    travel_taxi_services = config.travel_taxi_services 
    travel_theme_parks = config.travel_theme_parks 
    travel_tourism = config.travel_tourism 
    travel_tourist_destinations = config.travel_tourist_destinations 
    travel_tourist_gardens = config.travel_tourist_gardens 
    travel_travel = config.travel_travel 
    travel_travel_air_travel = config.travel_travel_air_travel 
    travel_travel_bus = config.travel_travel_bus 
    travel_travel_rail = config.travel_travel_rail 
    travel_travel_train = config.travel_travel_train 
    travel_vacation = config.travel_vacation 
    travel_vacation_rentals = config.travel_vacation_rentals 
    travel_zoos = config.travel_zoos 
    vehicle_autos = config.vehicle_autos 
    vehicle_bicycles = config.vehicle_bicycles 
    vehicle_bicycles_accessories = config.vehicle_bicycles_accessories 
    vehicle_bike_parts = config.vehicle_bike_parts 
    vehicle_bike_repair = config.vehicle_bike_repair 
    vehicle_bmx_accessories = config.vehicle_bmx_accessories 
    vehicle_bmx_bikes = config.vehicle_bmx_bikes 
    vehicle_boats = config.vehicle_boats 
    vehicle_buy_car = config.vehicle_buy_car 
    vehicle_buy_used_car = config.vehicle_buy_used_car 
    vehicle_campers = config.vehicle_campers 
    vehicle_car_shows = config.vehicle_car_shows 
    vehicle_cargo_trailers = config.vehicle_cargo_trailers 
    vehicle_cargo_trucks = config.vehicle_cargo_trucks 
    vehicle_classic_cars = config.vehicle_classic_cars 
    vehicle_driving_laws = config.vehicle_driving_laws 
    vehicle_driving_license = config.vehicle_driving_license 
    vehicle_electric_cars = config.vehicle_electric_cars 
    vehicle_gas_prices = config.vehicle_gas_prices 
    vehicle_hybrid_cars = config.vehicle_hybrid_cars 
    vehicle_jet_skis = config.vehicle_jet_skis 
    vehicle_motorcycles = config.vehicle_motorcycles 
    vehicle_off_road_vehicles = config.vehicle_off_road_vehicles 
    vehicle_sell_car = config.vehicle_sell_car 
    vehicle_sell_used_car = config.vehicle_sell_used_car 
    vehicle_suvs = config.vehicle_suvs 
    vehicle_trucks = config.vehicle_trucks 
    vehicle_vehicle_accessories = config.vehicle_vehicle_accessories 
    vehicle_vehicle_maintenance = config.vehicle_vehicle_maintenance 
    vehicle_vehicle_parts = config.vehicle_vehicle_parts 
    vehicle_vehicle_registration = config.vehicle_vehicle_registration 
    vehicle_vehicle_repair = config.vehicle_vehicle_repair 
    vehicle_vehicle_services = config.vehicle_vehicle_services 
    vehicle_watercraft = config.vehicle_watercraft 
    adult_orgasms = config.adult_orgasms 
    adult_penis_enlargement = config.adult_penis_enlargement 
    adult_sex = config.adult_sex 
    arts_contests = config.arts_contests 
    arts_metalwork = config.arts_metalwork 
    arts_paranormal = config.arts_paranormal 
    arts_woodwork = config.arts_woodwork 
    arts_writing = config.arts_writing 
    business_negotiations = config.business_negotiations 
    business_profession = config.business_profession 
    business_profits = config.business_profits 
    computers_virtual_reality = config.computers_virtual_reality 
    finance_benefits = config.finance_benefits 
    finance_taxes = config.finance_taxes 
    finance_wealth = config.finance_wealth 
    food_fruits = config.food_fruits 
    food_vegetables = config.food_vegetables 
    general_accidents = config.general_accidents 
    general_advice = config.general_advice 
    general_agreements = config.general_agreements 
    general_air_force = config.general_air_force 
    general_answers = config.general_answers 
    general_arguments = config.general_arguments 
    general_army = config.general_army 
    general_assistance = config.general_assistance 
    general_awareness = config.general_awareness 
    general_celebrations = config.general_celebrations 
    general_coast_guard = config.general_coast_guard 
    general_competition = config.general_competition 
    general_complaints = config.general_complaints 
    general_confusion = config.general_confusion 
    general_consequence = config.general_consequence 
    general_courage = config.general_courage 
    general_criticism = config.general_criticism 
    general_death = config.general_death 
    general_efficiency = config.general_efficiency 
    general_emergencies = config.general_emergencies 
    general_emotions = config.general_emotions 
    general_enthusiasm = config.general_enthusiasm 
    general_equipment = config.general_equipment 
    general_excitement = config.general_excitement 
    general_extermination = config.general_extermination 
    general_feedback = config.general_feedback 
    general_fortune = config.general_fortune 
    general_fun = config.general_fun 
    general_growth = config.general_growth 
    general_guide = config.general_guide 
    general_homework = config.general_homework 
    general_hope = config.general_hope 
    general_improvement = config.general_improvement 
    general_information = config.general_information 
    general_instruction = config.general_instruction 
    general_interest = config.general_interest 
    general_issues = config.general_issues 
    general_luck = config.general_luck 
    general_maintenance = config.general_maintenance 
    general_management = config.general_management 
    general_marines = config.general_marines 
    general_memberships = config.general_memberships 
    general_military = config.general_military 
    general_mind = config.general_mind 
    general_navy = config.general_navy 
    general_networking = config.general_networking 
    general_opinion = config.general_opinion 
    general_panic = config.general_panic 
    general_perception = config.general_perception 
    general_perspective = config.general_perspective 
    general_philosophy = config.general_philosophy 
    general_pollution = config.general_pollution 
    general_problems = config.general_problems 
    general_progress = config.general_progress 
    general_purpose = config.general_purpose 
    general_questions = config.general_questions 
    general_recommendations = config.general_recommendations 
    general_requirements = config.general_requirements 
    general_research = config.general_research 
    general_reviews = config.general_reviews 
    general_risk = config.general_risk 
    general_schools = config.general_schools 
    general_service = config.general_service 
    general_solutions = config.general_solutions 
    general_space_force = config.general_space_force 
    general_storage = config.general_storage 
    general_success = config.general_success 
    general_theories = config.general_theories 
    general_tools = config.general_tools 
    general_training = config.general_training 
    general_trouble = config.general_trouble 
    general_warning = config.general_warning 
    health_diseases = config.health_diseases 
    health_genes = config.health_genes 
    health_injury = config.health_injury 
    health_medicine = config.health_medicine 
    health_sports_injury = config.health_sports_injury 
    health_stroke = config.health_stroke 
    health_surgery = config.health_surgery 
    health_symptoms = config.health_symptoms 
    home_roofing = config.home_roofing 
    home_siding = config.home_siding 
    jobs_careers = config.jobs_careers 
    jobs_employment = config.jobs_employment 
    law_evidence = config.law_evidence 
    news_magazines = config.news_magazines 
    news_news_politics_capitalism = config.news_news_politics_capitalism 
    news_news_politics_feminism = config.news_news_politics_feminism 
    news_news_politics_libertarianism = config.news_news_politics_libertarianism 
    news_news_politics_socialism = config.news_news_politics_socialism 
    news_newspapers = config.news_newspapers 
    reference_languages = config.reference_languages 
    science_laboratory = config.science_laboratory 
    science_nature = config.science_nature 
    science_planets = config.science_planets 
    society_babies = config.society_babies 
    society_charity = config.society_charity 
    society_childhood = config.society_childhood 
    society_church = config.society_church 
    society_culture = config.society_culture 
    society_debates = config.society_debates 
    society_dependents = config.society_dependents 
    society_family_relationship_husband = config.society_family_relationship_husband 
    society_friendship = config.society_friendship 
    society_funeral = config.society_funeral 
    society_leadership = config.society_leadership 
    society_life = config.society_life 
    society_living = config.society_living 
    society_love = config.society_love 
    society_men = config.society_men 
    society_obligation = config.society_obligation 
    society_peace = config.society_peace 
    society_sympathy = config.society_sympathy 
    society_teaching = config.society_teaching 
    society_traditions = config.society_traditions 
    society_war_crimes = config.society_war_crimes 
    society_women = config.society_women 
    sports_championships = config.sports_championships 
    travel_tours = config.travel_tours 

    async def propnoun_func():
        for token1 in nlp_title:
            if token1.pos_ == 'PROPN':
                PROPN_list.append(token1.lemma_) 
    async def noun_func():
        for token in nlp_title:
            if token.pos_ == 'NOUN':
                PROPN_list.append(token.lemma_) 
    async def sent_func():
        
        senti_tolks = {}
        for sent in doc.sents:
            senty_tolk_lister = []
            senti = nlp(sent.text)
            sia = SentimentIntensityAnalyzer()
            sentiment = sia.polarity_scores(sent.text)
            for pos__ in senti:
                ent_lister = []
                for ent in senti.ents:            
                    ent_tolks = {
                        "Entity" : ent.text,
                        "start_char" : ent.start_char, 
                        "end_char" : ent.end_char, 
                        "label_" : ent.label_
                                }   
                    ent_lister.append(ent_tolks)
                senti_tolks = {
                    "Tolken" : pos__.text,
                    "Lemma" : pos__.lemma_,
                    "Part_Of_Speech" : pos__.pos_,
                    "POS_tag" : pos__.tag_,
                    "POS_dep" : pos__.dep_
                            }
                senty_tolk_lister.append(senti_tolks)
                sentence = {"sentence" : sent.text, "sentiment" : sentiment, "sentence_tolken_list" : senty_tolk_lister, "entity_list": ent_lister}
            sentences_list.append(sentence)
        senty_lister = {"sentences_list" : sentences_list}
        hh = [d['sentence_tolken_list'] for d in sentences_list]
        
        for hhh in hh:
            for hhhh in hhh:
                if hhhh['Part_Of_Speech'] == 'PROPN':
                    PROPN_list.append(hhhh['Lemma'])
        ii = [d['entity_list'] for d in sentences_list]
        for iii in ii:
            for iiii in iii:
                if iiii['label_'] =='ORG':
                    PROPN_list.append(iiii['Entity'])
        return senty_lister     
    async def async_bi():
        bigrams = nltk.bigrams(wordsCL)
        freq_bi = nltk.FreqDist(bigrams)
        bi_tup = list(freq_bi.most_common(12))
        for bi in bi_tup:
            bi_nlp = ' '.join(bi[0])
            bi_list.append(bi_nlp)
            PROPN_list.append(bi_nlp)
    async def async_tri():
        trigrams = nltk.trigrams(wordsCL)
        freq_tri = nltk.FreqDist(trigrams)  
        tri_tup = list(freq_tri.most_common(12))
        for tri in tri_tup:
            tri_nlp = ' '.join(tri[0])
            tri_list.append(tri_nlp)
            PROPN_list.append(tri_nlp)  
    async def async_rake():
        rake_object = RAKE.Rake(stop)
        def Sort_Tuple(tup):
            tup.sort(key = lambda x: x[1])
            return tup
        keywords = Sort_Tuple(rake_object.run(corp_list_joined.lower()))[-10:]
        keywords = dict(keywords)
        for kw,v in keywords.items():
            rake_list.append(kw)
            PROPN_list.append(kw)

    async def thinker(check_word_ch):
        
        nlp_title_list = []
        check_word = nlp(str(check_word_ch))
        check_word_str = check_word.text
        nlp_title_list.append((check_word.similarity(adult), check_word_str, 'Adult'))
        nlp_title_list.append((check_word.similarity(adult_breast_enlargement), check_word_str, 'Adult, Breast Enlargement'))
        nlp_title_list.append((check_word.similarity(adult_condoms), check_word_str, 'Adult, Condoms'))
        nlp_title_list.append((check_word.similarity(adult_contraception), check_word_str, 'Adult, Contraception'))
        nlp_title_list.append((check_word.similarity(adult_erection), check_word_str, 'Adult, Erections'))
        nlp_title_list.append((check_word.similarity(adult_orgasms), check_word_str, 'Adult, Sexual Orgasm'))
        nlp_title_list.append((check_word.similarity(adult_penis_enlargement), check_word_str, 'Adult, Penis Enlargement'))
        nlp_title_list.append((check_word.similarity(adult_prostitution), check_word_str, 'Adult, Prostitution'))
        nlp_title_list.append((check_word.similarity(adult_sex), check_word_str, 'Adult, Adult Sex'))
        nlp_title_list.append((check_word.similarity(animals_animals), check_word_str, 'Animals, Animals'))
        nlp_title_list.append((check_word.similarity(animals_birds), check_word_str, 'Animals, Birds'))
        nlp_title_list.append((check_word.similarity(animals_cats), check_word_str, 'Animals, Cats'))
        nlp_title_list.append((check_word.similarity(animals_dogs), check_word_str, 'Animals, Dogs'))
        nlp_title_list.append((check_word.similarity(animals_exotic_animals), check_word_str, 'Animals, Exotic Animals'))
        nlp_title_list.append((check_word.similarity(animals_exotic_pets), check_word_str, 'Animals, Exotic Pets'))
        nlp_title_list.append((check_word.similarity(animals_fish_aquaria), check_word_str, 'Animals, Fish Aquaria'))
        nlp_title_list.append((check_word.similarity(animals_horses), check_word_str, 'Animals, Horses'))
        nlp_title_list.append((check_word.similarity(animals_pet_food), check_word_str, 'Animals, Pet Food'))
        nlp_title_list.append((check_word.similarity(animals_pet_products), check_word_str, 'Animals, Pet Products'))
        nlp_title_list.append((check_word.similarity(animals_pet_supplies), check_word_str, 'Animals, Pet Supplies'))
        nlp_title_list.append((check_word.similarity(animals_pets), check_word_str, 'Animals, Pets'))
        nlp_title_list.append((check_word.similarity(animals_pets_amphibians), check_word_str, 'Animals, Pets Amphibians'))
        nlp_title_list.append((check_word.similarity(animals_pets_fish), check_word_str, 'Animals, Pets Fish'))
        nlp_title_list.append((check_word.similarity(animals_pets_rabbits), check_word_str, 'Animals, Pets Rabbits'))
        nlp_title_list.append((check_word.similarity(animals_pets_reptiles), check_word_str, 'Animals, Pets Reptiles'))
        nlp_title_list.append((check_word.similarity(animals_pets_rodents), check_word_str, 'Animals, Pets Rodents'))
        nlp_title_list.append((check_word.similarity(animals_veterinarians), check_word_str, 'Animals, Veterinarians'))
        nlp_title_list.append((check_word.similarity(animals_wildlife), check_word_str, 'Animals, Wildlife'))
        nlp_title_list.append((check_word.similarity(arts_acting), check_word_str, 'Arts & Entertainment, Acting'))
        nlp_title_list.append((check_word.similarity(arts_animation), check_word_str, 'Arts & Entertainment, Animation'))
        nlp_title_list.append((check_word.similarity(arts_anime), check_word_str, 'Arts & Entertainment, Anime'))
        nlp_title_list.append((check_word.similarity(arts_architecture), check_word_str, 'Arts & Entertainment, Architecture'))
        nlp_title_list.append((check_word.similarity(arts_art_galleries), check_word_str, 'Arts & Entertainment, Art Galleries'))
        nlp_title_list.append((check_word.similarity(arts_art_museums), check_word_str, 'Arts & Entertainment, Art Museums'))
        nlp_title_list.append((check_word.similarity(arts_arts), check_word_str, 'Arts & Entertainment, Arts'))
        nlp_title_list.append((check_word.similarity(arts_audio_equipment), check_word_str, 'Arts & Entertainment, Audio Equipment'))
        nlp_title_list.append((check_word.similarity(arts_bars_listings), check_word_str, 'Arts & Entertainment, Bars Listings'))
        nlp_title_list.append((check_word.similarity(arts_blues_music), check_word_str, 'Arts & Entertainment, Blues Music'))
        nlp_title_list.append((check_word.similarity(arts_cartoons), check_word_str, 'Arts & Entertainment, Cartoons'))
        nlp_title_list.append((check_word.similarity(arts_cd_shopping), check_word_str, 'Arts & Entertainment, Cd Shopping'))
        nlp_title_list.append((check_word.similarity(arts_celebrities), check_word_str, 'Arts & Entertainment, Celebrities'))
        nlp_title_list.append((check_word.similarity(arts_circus), check_word_str, 'Arts & Entertainment, Circus'))
        nlp_title_list.append((check_word.similarity(arts_classical_music), check_word_str, 'Arts & Entertainment, Classical Music'))
        nlp_title_list.append((check_word.similarity(arts_clubs_listings), check_word_str, 'Arts & Entertainment, Clubs Listings'))
        nlp_title_list.append((check_word.similarity(arts_coloring), check_word_str, 'Arts & Entertainment, Coloring'))
        nlp_title_list.append((check_word.similarity(arts_comics), check_word_str, 'Arts & Entertainment, Comics'))
        nlp_title_list.append((check_word.similarity(arts_concerts), check_word_str, 'Arts & Entertainment, Concerts'))
        nlp_title_list.append((check_word.similarity(arts_contests), check_word_str, 'Arts & Entertainment, Contests'))
        nlp_title_list.append((check_word.similarity(arts_conventions), check_word_str, 'Arts & Entertainment, Conventions'))
        nlp_title_list.append((check_word.similarity(arts_country_music), check_word_str, 'Arts & Entertainment, Country Music'))
        nlp_title_list.append((check_word.similarity(arts_dance_electronic_music), check_word_str, 'Arts & Entertainment, Dance Electronic Music'))
        nlp_title_list.append((check_word.similarity(arts_design), check_word_str, 'Arts & Entertainment, Design'))
        nlp_title_list.append((check_word.similarity(arts_digital_art), check_word_str, 'Arts & Entertainment, Digital Art'))
        nlp_title_list.append((check_word.similarity(arts_drawing), check_word_str, 'Arts & Entertainment, Drawing'))
        nlp_title_list.append((check_word.similarity(arts_entertainment), check_word_str, 'Arts & Entertainment, Entertainment'))
        nlp_title_list.append((check_word.similarity(arts_entertainment_industry), check_word_str, 'Arts & Entertainment, Entertainment Industry'))
        nlp_title_list.append((check_word.similarity(arts_events_listings), check_word_str, 'Arts & Entertainment, Events Listings'))
        nlp_title_list.append((check_word.similarity(arts_experimental_music), check_word_str, 'Arts & Entertainment, Experimental Music'))
        nlp_title_list.append((check_word.similarity(arts_expos), check_word_str, 'Arts & Entertainment, Expos'))
        nlp_title_list.append((check_word.similarity(arts_festivals), check_word_str, 'Arts & Entertainment, Festivals'))
        nlp_title_list.append((check_word.similarity(arts_film_festivals), check_word_str, 'Arts & Entertainment, Film Festivals'))
        nlp_title_list.append((check_word.similarity(arts_film_industry), check_word_str, 'Arts & Entertainment, Film Industry'))
        nlp_title_list.append((check_word.similarity(arts_flash_trivia), check_word_str, 'Arts & Entertainment, Flash Trivia'))
        nlp_title_list.append((check_word.similarity(arts_funny_pictures), check_word_str, 'Arts & Entertainment, Funny Pictures'))
        nlp_title_list.append((check_word.similarity(arts_funny_videos), check_word_str, 'Arts & Entertainment, Funny Videos'))
        nlp_title_list.append((check_word.similarity(arts_hip_hop), check_word_str, 'Arts & Entertainment, Hip Hop'))
        nlp_title_list.append((check_word.similarity(arts_humor), check_word_str, 'Arts & Entertainment, Humor'))
        nlp_title_list.append((check_word.similarity(arts_image_galleries), check_word_str, 'Arts & Entertainment, Image Galleries'))
        nlp_title_list.append((check_word.similarity(arts_industrial_music), check_word_str, 'Arts & Entertainment, Industrial Music'))
        nlp_title_list.append((check_word.similarity(arts_jazz_music), check_word_str, 'Arts & Entertainment, Jazz Music'))
        nlp_title_list.append((check_word.similarity(arts_magic), check_word_str, 'Arts & Entertainment, Magic'))
        nlp_title_list.append((check_word.similarity(arts_manga), check_word_str, 'Arts & Entertainment, Manga'))
        nlp_title_list.append((check_word.similarity(arts_memes), check_word_str, 'Arts & Entertainment, Memes'))
        nlp_title_list.append((check_word.similarity(arts_metalwork), check_word_str, 'Arts & Entertainment, Metalworking'))
        nlp_title_list.append((check_word.similarity(arts_movie_showtimes), check_word_str, 'Arts & Entertainment, Movie Showtimes'))
        nlp_title_list.append((check_word.similarity(arts_movie_soundtracks), check_word_str, 'Arts & Entertainment, Movie Soundtracks'))
        nlp_title_list.append((check_word.similarity(arts_movies), check_word_str, 'Arts & Entertainment, Movies'))
        nlp_title_list.append((check_word.similarity(arts_music), check_word_str, 'Arts & Entertainment, Music'))
        nlp_title_list.append((check_word.similarity(arts_music_downloads), check_word_str, 'Arts & Entertainment, Music Downloads'))
        nlp_title_list.append((check_word.similarity(arts_music_instruction), check_word_str, 'Arts & Entertainment, Music Instruction'))
        nlp_title_list.append((check_word.similarity(arts_music_instruction_bass), check_word_str, 'Arts & Entertainment, Bass Guitar'))
        nlp_title_list.append((check_word.similarity(arts_music_instruction_drums), check_word_str, 'Arts & Entertainment, Drums'))
        nlp_title_list.append((check_word.similarity(arts_music_instruction_keyboard), check_word_str, 'Arts & Entertainment, Keyboard'))
        nlp_title_list.append((check_word.similarity(arts_music_instrument_guitar), check_word_str, 'Arts & Entertainment, Guitar'))
        nlp_title_list.append((check_word.similarity(arts_music_reference), check_word_str, 'Arts & Entertainment, Music Reference'))
        nlp_title_list.append((check_word.similarity(arts_music_streams), check_word_str, 'Arts & Entertainment, Music Streams'))
        nlp_title_list.append((check_word.similarity(arts_music_videos), check_word_str, 'Arts & Entertainment, Music Videos'))
        nlp_title_list.append((check_word.similarity(arts_nightlife), check_word_str, 'Arts & Entertainment, Nightlife'))
        nlp_title_list.append((check_word.similarity(arts_occult), check_word_str, 'Arts & Entertainment, Occult'))
        nlp_title_list.append((check_word.similarity(arts_offbeat), check_word_str, 'Arts & Entertainment, Offbeat'))
        nlp_title_list.append((check_word.similarity(arts_online_media), check_word_str, 'Arts & Entertainment, Online Media'))
        nlp_title_list.append((check_word.similarity(arts_online_video), check_word_str, 'Arts & Entertainment, Online Video'))
        nlp_title_list.append((check_word.similarity(arts_opera), check_word_str, 'Arts & Entertainment, Opera'))
        nlp_title_list.append((check_word.similarity(arts_painting), check_word_str, 'Arts & Entertainment, Painting'))
        nlp_title_list.append((check_word.similarity(arts_paranormal), check_word_str, 'Arts & Entertainment, Paranormal'))
        nlp_title_list.append((check_word.similarity(arts_performing_arts), check_word_str, 'Arts & Entertainment, Performing Arts'))
        nlp_title_list.append((check_word.similarity(arts_photgraphy), check_word_str, 'Arts & Entertainment, Photography'))
        nlp_title_list.append((check_word.similarity(arts_political_humor), check_word_str, 'Arts & Entertainment, Political Humor'))
        nlp_title_list.append((check_word.similarity(arts_pop_music), check_word_str, 'Arts & Entertainment, Pop Music'))
        nlp_title_list.append((check_word.similarity(arts_radio_music), check_word_str, 'Arts & Entertainment, Radio Music'))
        nlp_title_list.append((check_word.similarity(arts_recording_industry), check_word_str, 'Arts & Entertainment, Recording Industry'))
        nlp_title_list.append((check_word.similarity(arts_religious_music), check_word_str, 'Arts & Entertainment, Religious Music'))
        nlp_title_list.append((check_word.similarity(arts_rock_music), check_word_str, 'Arts & Entertainment, Rock Music'))
        nlp_title_list.append((check_word.similarity(arts_surveys), check_word_str, 'Arts & Entertainment, Surveys'))
        nlp_title_list.append((check_word.similarity(arts_trivia), check_word_str, 'Arts & Entertainment, Trivia'))
        nlp_title_list.append((check_word.similarity(arts_tv), check_word_str, 'Arts & Entertainment, TV'))
        nlp_title_list.append((check_word.similarity(arts_tv_commercials), check_word_str, 'Arts & Entertainment, TV Commercials'))
        nlp_title_list.append((check_word.similarity(arts_tv_industry), check_word_str, 'Arts & Entertainment, TV Industry'))
        nlp_title_list.append((check_word.similarity(arts_tv_shows), check_word_str, 'Arts & Entertainment, TV Shows'))
        nlp_title_list.append((check_word.similarity(arts_visual_art), check_word_str, 'Arts & Entertainment, Visual Art'))
        nlp_title_list.append((check_word.similarity(arts_woodwork), check_word_str, 'Arts & Entertainment, Woodwork'))
        nlp_title_list.append((check_word.similarity(arts_writing), check_word_str, 'Arts & Entertainment, Writing'))
        nlp_title_list.append((check_word.similarity(beauty_beauty), check_word_str, 'Beauty, Beauty'))
        nlp_title_list.append((check_word.similarity(beauty_beauty_pageants), check_word_str, 'Beauty, Beauty Pageants'))
        nlp_title_list.append((check_word.similarity(beauty_body_art), check_word_str, 'Beauty, Body Art'))
        nlp_title_list.append((check_word.similarity(beauty_body_care), check_word_str, 'Beauty, Body Care'))
        nlp_title_list.append((check_word.similarity(beauty_cosmetic_procedures), check_word_str, 'Beauty, Cosmetic Procedures'))
        nlp_title_list.append((check_word.similarity(beauty_cosmetic_surgery), check_word_str, 'Beauty, Cosmetic Surgery'))
        nlp_title_list.append((check_word.similarity(beauty_cosmetics), check_word_str, 'Beauty, Cosmetics'))
        nlp_title_list.append((check_word.similarity(beauty_cosmetology), check_word_str, 'Beauty, Cosmetology'))
        nlp_title_list.append((check_word.similarity(beauty_exercise), check_word_str, 'Beauty, Exercise'))
        nlp_title_list.append((check_word.similarity(beauty_exercise_equipment), check_word_str, 'Beauty, Exercise Equipment'))
        nlp_title_list.append((check_word.similarity(beauty_face_care), check_word_str, 'Beauty, Face Care'))
        nlp_title_list.append((check_word.similarity(beauty_fashion), check_word_str, 'Beauty, Fashion'))
        nlp_title_list.append((check_word.similarity(beauty_fashion_collections), check_word_str, 'Beauty, Fashion Collections'))
        nlp_title_list.append((check_word.similarity(beauty_fitness), check_word_str, 'Beauty, Fitness'))
        nlp_title_list.append((check_word.similarity(beauty_fitness_antioxidants), check_word_str, 'Beauty, Antioxidants'))
        nlp_title_list.append((check_word.similarity(beauty_hair_care), check_word_str, 'Beauty, Hair Care'))
        nlp_title_list.append((check_word.similarity(beauty_hair_loss), check_word_str, 'Beauty, Hair Loss'))
        nlp_title_list.append((check_word.similarity(beauty_hair_removal), check_word_str, 'Beauty, Hair Removal'))
        nlp_title_list.append((check_word.similarity(beauty_hygiene_products), check_word_str, 'Beauty, Hygiene Products'))
        nlp_title_list.append((check_word.similarity(beauty_massage), check_word_str, 'Beauty, Massage'))
        nlp_title_list.append((check_word.similarity(beauty_nail_care), check_word_str, 'Beauty, Nail Care'))
        nlp_title_list.append((check_word.similarity(beauty_perfumes), check_word_str, 'Beauty, Perfumes'))
        nlp_title_list.append((check_word.similarity(beauty_skin_care), check_word_str, 'Beauty, Skin Care'))
        nlp_title_list.append((check_word.similarity(beauty_spas), check_word_str, 'Beauty, Spas'))
        nlp_title_list.append((check_word.similarity(beauty_weight_loss), check_word_str, 'Beauty, Weight Loss'))
        nlp_title_list.append((check_word.similarity(books_books), check_word_str, 'Books, Books'))
        nlp_title_list.append((check_word.similarity(books_children_books), check_word_str, 'Books, Children Books'))
        nlp_title_list.append((check_word.similarity(books_e_books), check_word_str, 'Books, E Books'))
        nlp_title_list.append((check_word.similarity(books_fan_fiction), check_word_str, 'Books, Fan Fiction'))
        nlp_title_list.append((check_word.similarity(books_literary_classics), check_word_str, 'Books, Literary Classics'))
        nlp_title_list.append((check_word.similarity(books_poetry), check_word_str, 'Books, Poetry'))
        nlp_title_list.append((check_word.similarity(books_writers_resources), check_word_str, 'Books, Writers Resources'))
        nlp_title_list.append((check_word.similarity(business_advertising), check_word_str, 'Business & Industry, Advertising'))
        nlp_title_list.append((check_word.similarity(business_aerospace), check_word_str, 'Business & Industry, Aerospace'))
        nlp_title_list.append((check_word.similarity(business_affiliate_marketing), check_word_str, 'Business & Industry, Affiliate Marketing'))
        nlp_title_list.append((check_word.similarity(business_agricultural_equipment), check_word_str, 'Business & Industry, Agricultural Equipment'))
        nlp_title_list.append((check_word.similarity(business_agriculture), check_word_str, 'Business & Industry, Agriculture'))
        nlp_title_list.append((check_word.similarity(business_alternative_energy), check_word_str, 'Business & Industry, Alternative Energy'))
        nlp_title_list.append((check_word.similarity(business_automotive_industry), check_word_str, 'Business & Industry, Automotive Industry'))
        nlp_title_list.append((check_word.similarity(business_biotech_industry), check_word_str, 'Business & Industry, Biotech Industry'))
        nlp_title_list.append((check_word.similarity(business_business), check_word_str, 'Business & Industry, Business'))
        nlp_title_list.append((check_word.similarity(business_business_capital), check_word_str, 'Business & Industry, Business Capital'))
        nlp_title_list.append((check_word.similarity(business_business_consulting), check_word_str, 'Business & Industry, Business Consulting'))
        nlp_title_list.append((check_word.similarity(business_business_education), check_word_str, 'Business & Industry, Business Education'))
        nlp_title_list.append((check_word.similarity(business_business_fire_security), check_word_str, 'Business & Industry, Business Fire Security'))
        nlp_title_list.append((check_word.similarity(business_business_management), check_word_str, 'Business & Industry, Business Management'))
        nlp_title_list.append((check_word.similarity(business_business_operations), check_word_str, 'Business & Industry, Business Operations'))
        nlp_title_list.append((check_word.similarity(business_business_plans), check_word_str, 'Business & Industry, Business Plans'))
        nlp_title_list.append((check_word.similarity(business_business_presentations), check_word_str, 'Business & Industry, Business Presentations'))
        nlp_title_list.append((check_word.similarity(business_business_services), check_word_str, 'Business & Industry, Business Services'))
        nlp_title_list.append((check_word.similarity(business_business_venture), check_word_str, 'Business & Industry, Business Venture'))
        nlp_title_list.append((check_word.similarity(business_chemical_industry), check_word_str, 'Business & Industry, Chemical Industry'))
        nlp_title_list.append((check_word.similarity(business_cleaning_agents_industry), check_word_str, 'Business & Industry, Cleaning Agents Industry'))
        nlp_title_list.append((check_word.similarity(business_commercial_vehicle), check_word_str, 'Business & Industry, Commercial Vehicles'))
        nlp_title_list.append((check_word.similarity(business_construction), check_word_str, 'Business & Industry, Construction'))
        nlp_title_list.append((check_word.similarity(business_construction_materials), check_word_str, 'Business & Industry, Construction Materials'))
        nlp_title_list.append((check_word.similarity(business_corporate_events), check_word_str, 'Business & Industry, Corporate Events'))
        nlp_title_list.append((check_word.similarity(business_defense_technology), check_word_str, 'Business & Industry, Defense Technology'))
        nlp_title_list.append((check_word.similarity(business_delivery_industry ), check_word_str, 'Business & Industry, Delivery Industry'))
        nlp_title_list.append((check_word.similarity(business_e_commerce), check_word_str, 'Business & Industry, E Commerce'))
        nlp_title_list.append((check_word.similarity(business_editing_services), check_word_str, 'Business & Industry, Editing Services'))
        nlp_title_list.append((check_word.similarity(business_electricity_services), check_word_str, 'Business & Industry, Electricity Services'))
        nlp_title_list.append((check_word.similarity(business_energy_industry), check_word_str, 'Business & Industry, Energy Industry'))
        nlp_title_list.append((check_word.similarity(business_event_planning), check_word_str, 'Business & Industry, Event Planning'))
        nlp_title_list.append((check_word.similarity(business_finance_industry), check_word_str, 'Business & Industry, Finance Industry'))
        nlp_title_list.append((check_word.similarity(business_food_service), check_word_str, 'Business & Industry, Food Service'))
        nlp_title_list.append((check_word.similarity(business_forestry_industry), check_word_str, 'Business & Industry, Forestry Industry'))
        nlp_title_list.append((check_word.similarity(business_freight_industry), check_word_str, 'Business & Industry, Freight Industry'))
        nlp_title_list.append((check_word.similarity(business_gas_industry), check_word_str, 'Business & Industry, Gas Industry'))
        nlp_title_list.append((check_word.similarity(business_heavy_equipment_industry), check_word_str, 'Business & Industry, Heavy Equipment Industry'))
        nlp_title_list.append((check_word.similarity(business_hospitality_industry), check_word_str, 'Business & Industry, Hospitality Industry'))
        nlp_title_list.append((check_word.similarity(business_hospitality_planning), check_word_str, 'Business & Industry, Hospitality Planning'))
        nlp_title_list.append((check_word.similarity(business_industrial_equipment), check_word_str, 'Business & Industry, Industrial Equipment'))
        nlp_title_list.append((check_word.similarity(business_industry), check_word_str, 'Business & Industry, Industry'))
        nlp_title_list.append((check_word.similarity(business_livestock_industry), check_word_str, 'Business & Industry, Livestock Industry'))
        nlp_title_list.append((check_word.similarity(business_logistics_industry), check_word_str, 'Business & Industry, Logistics Industry'))
        nlp_title_list.append((check_word.similarity(business_maintenance_industry), check_word_str, 'Business & Industry, Maintenance Industry'))
        nlp_title_list.append((check_word.similarity(business_manufacturing_industry), check_word_str, 'Business & Industry, Manufacturing Industry'))
        nlp_title_list.append((check_word.similarity(business_maritime_transport), check_word_str, 'Business & Industry, Maritime Transport'))
        nlp_title_list.append((check_word.similarity(business_marketing), check_word_str, 'Business & Industry, Marketing'))
        nlp_title_list.append((check_word.similarity(business_metals_mining_industry), check_word_str, 'Business & Industry, Metals Mining Industry'))
        nlp_title_list.append((check_word.similarity(business_mining_industry), check_word_str, 'Business & Industry, Mining Industry'))
        nlp_title_list.append((check_word.similarity(business_mining_precious_metals_industry), check_word_str, 'Business & Industry, Mining Precious Metals Industry'))
        nlp_title_list.append((check_word.similarity(business_mlm), check_word_str, 'Business & Industry, Mlm'))
        nlp_title_list.append((check_word.similarity(business_moving_industry), check_word_str, 'Business & Industry, Moving Industry'))
        nlp_title_list.append((check_word.similarity(business_negotiations), check_word_str, 'Business & Industry, Negotiations'))
        nlp_title_list.append((check_word.similarity(business_nonwovens_industry), check_word_str, 'Business & Industry, Nonwovens Industry'))
        nlp_title_list.append((check_word.similarity(business_office_services), check_word_str, 'Business & Industry, Office Services'))
        nlp_title_list.append((check_word.similarity(business_office_supplies), check_word_str, 'Business & Industry, Office Supplies'))
        nlp_title_list.append((check_word.similarity(business_oil), check_word_str, 'Business & Industry, Oil'))
        nlp_title_list.append((check_word.similarity(business_oil_industry), check_word_str, 'Business & Industry, Oil Industry'))
        nlp_title_list.append((check_word.similarity(business_online_business), check_word_str, 'Business & Industry, Online Business'))
        nlp_title_list.append((check_word.similarity(business_packaging_industry), check_word_str, 'Business & Industry, Packaging Industry'))
        nlp_title_list.append((check_word.similarity(business_parking), check_word_str, 'Business & Industry, Parking'))
        nlp_title_list.append((check_word.similarity(business_pharmaceuticals_industry), check_word_str, 'Business & Industry, Pharmaceuticals Industry'))
        nlp_title_list.append((check_word.similarity(business_plastics_industry), check_word_str, 'Business & Industry, Plastics Industry'))
        nlp_title_list.append((check_word.similarity(business_polymers_industry), check_word_str, 'Business & Industry, Polymers Industry'))
        nlp_title_list.append((check_word.similarity(business_powerwasher), check_word_str, 'Business & Industry, Power Washing'))
        nlp_title_list.append((check_word.similarity(business_printing_industry), check_word_str, 'Business & Industry, Printing Industry'))
        nlp_title_list.append((check_word.similarity(business_profession), check_word_str, 'Business & Industry, Business Profession'))
        nlp_title_list.append((check_word.similarity(business_profits), check_word_str, 'Business & Industry, Business Profits'))
        nlp_title_list.append((check_word.similarity(business_public_relations), check_word_str, 'Business & Industry, Public Relations'))
        nlp_title_list.append((check_word.similarity(business_public_transportation), check_word_str, 'Business & Industry, Public Transportation'))
        nlp_title_list.append((check_word.similarity(business_publishing_industry), check_word_str, 'Business & Industry, Publishing Industry'))
        nlp_title_list.append((check_word.similarity(business_rail_transport), check_word_str, 'Business & Industry, Rail Transport'))
        nlp_title_list.append((check_word.similarity(business_renewable_energy), check_word_str, 'Business & Industry, Renewable Energy'))
        nlp_title_list.append((check_word.similarity(business_retail_equipment), check_word_str, 'Business & Industry, Retail Equipment'))
        nlp_title_list.append((check_word.similarity(business_retail_industry), check_word_str, 'Business & Industry, Retail Industry'))
        nlp_title_list.append((check_word.similarity(business_security), check_word_str, 'Business & Industry, Business Security'))
        nlp_title_list.append((check_word.similarity(business_small_business), check_word_str, 'Business & Industry, Small Business'))
        nlp_title_list.append((check_word.similarity(business_space_technology), check_word_str, 'Business & Industry, Space Technology'))
        nlp_title_list.append((check_word.similarity(business_textiles_industry), check_word_str, 'Business & Industry, Textiles Industry'))
        nlp_title_list.append((check_word.similarity(business_trade_industry), check_word_str, 'Business & Industry, Trade Industry'))
        nlp_title_list.append((check_word.similarity(business_transportation_industry), check_word_str, 'Business & Industry, Transportation Industry'))
        nlp_title_list.append((check_word.similarity(business_truckin_industry), check_word_str, 'Business & Industry, Truckin Industry'))
        nlp_title_list.append((check_word.similarity(business_urban_transportation), check_word_str, 'Business & Industry, Urban Transportation'))
        nlp_title_list.append((check_word.similarity(business_utilities_industry), check_word_str, 'Business & Industry, Utilities Industry'))
        nlp_title_list.append((check_word.similarity(business_writing_services), check_word_str, 'Business & Industry, Writing Services'))
        nlp_title_list.append((check_word.similarity(computer_bluetooth), check_word_str, 'Computers & Electronics, Bluetooth'))
        nlp_title_list.append((check_word.similarity(computers_apple_computer), check_word_str, 'Computers & Electronics, Apple Computers'))
        nlp_title_list.append((check_word.similarity(computers_audio_equipment), check_word_str, 'Computers & Electronics, Audio Equipment'))
        nlp_title_list.append((check_word.similarity(computers_business_software), check_word_str, 'Computers & Electronics, Business Software'))
        nlp_title_list.append((check_word.similarity(computers_c_language), check_word_str, 'Computers & Electronics, C Language'))
        nlp_title_list.append((check_word.similarity(computers_cad_cam), check_word_str, 'Computers & Electronics, Cad Cam'))
        nlp_title_list.append((check_word.similarity(computers_camera), check_word_str, 'Computers & Electronics, Cameras'))
        nlp_title_list.append((check_word.similarity(computers_camera_equipment), check_word_str, 'Computers & Electronics, Camera Equipment'))
        nlp_title_list.append((check_word.similarity(computers_car_electronics), check_word_str, 'Computers & Electronics, Car Electronics'))
        nlp_title_list.append((check_word.similarity(computers_computer_components), check_word_str, 'Computers & Electronics, Computer Components'))
        nlp_title_list.append((check_word.similarity(computers_computer_drives_storage), check_word_str, 'Computers & Electronics, Computer Drives Storage'))
        nlp_title_list.append((check_word.similarity(computers_computer_hacking), check_word_str, 'Computers & Electronics, Computer Hacking'))
        nlp_title_list.append((check_word.similarity(computers_computer_hardware), check_word_str, 'Computers & Electronics, Computer Hardware'))
        nlp_title_list.append((check_word.similarity(computers_computer_networking), check_word_str, 'Computers & Electronics, Computer Networking'))
        nlp_title_list.append((check_word.similarity(computers_computer_peripherals), check_word_str, 'Computers & Electronics, Computer Peripherals'))
        nlp_title_list.append((check_word.similarity(computers_computer_security), check_word_str, 'Computers & Electronics, Computer Security'))
        nlp_title_list.append((check_word.similarity(computers_surveillance_camera), check_word_str, 'Computers & Electronics, Surveillance Cameras'))
        nlp_title_list.append((check_word.similarity(computers_computers), check_word_str, 'Computers & Electronics, Computers'))
        nlp_title_list.append((check_word.similarity(computers_computers_programming), check_word_str, 'Computers & Electronics, Computers Programming'))
        nlp_title_list.append((check_word.similarity(computers_computers_software), check_word_str, 'Computers & Electronics, Computers Software'))
        nlp_title_list.append((check_word.similarity(computers_consumer_electronics), check_word_str, 'Computers & Electronics, Consumer Electronics'))
        nlp_title_list.append((check_word.similarity(computers_data_management), check_word_str, 'Computers & Electronics, Data Management'))
        nlp_title_list.append((check_word.similarity(computers_dedicated_server), check_word_str, 'Computers & Electronics, Dedicated Server'))
        nlp_title_list.append((check_word.similarity(computers_desktop_computers), check_word_str, 'Computers & Electronics, Desktop Computers'))
        nlp_title_list.append((check_word.similarity(computers_drones), check_word_str, 'Computers & Electronics, Drones'))
        nlp_title_list.append((check_word.similarity(computers_electronic_components), check_word_str, 'Computers & Electronics, Electronic Components'))
        nlp_title_list.append((check_word.similarity(computers_electronics), check_word_str, 'Computers & Electronics, Electronics'))
        nlp_title_list.append((check_word.similarity(computers_elm_language), check_word_str, 'Computers & Electronics, Elm Language'))
        nlp_title_list.append((check_word.similarity(computers_enterprise_technology), check_word_str, 'Computers & Electronics, Enterprise Technology'))
        nlp_title_list.append((check_word.similarity(computers_game_consoles), check_word_str, 'Computers & Electronics, Game Consoles'))
        nlp_title_list.append((check_word.similarity(computers_go_language), check_word_str, 'Computers & Electronics, Go Language'))
        nlp_title_list.append((check_word.similarity(computers_gps_navigation), check_word_str, 'Computers & Electronics, Gps Navigation'))
        nlp_title_list.append((check_word.similarity(computers_hd), check_word_str, 'Computers & Electronics, High-Definition Resolution'))
        nlp_title_list.append((check_word.similarity(computers_hosting), check_word_str, 'Computers & Electronics, Web Hosting'))
        nlp_title_list.append((check_word.similarity(computers_image_software), check_word_str, 'Computers & Electronics, Image Software'))
        nlp_title_list.append((check_word.similarity(computers_internet_software), check_word_str, 'Computers & Electronics, Internet Software'))
        nlp_title_list.append((check_word.similarity(computers_it), check_word_str, 'Computers & Electronics, IT'))
        nlp_title_list.append((check_word.similarity(computers_java_language), check_word_str, 'Computers & Electronics, Java Language'))
        nlp_title_list.append((check_word.similarity(computers_javascript_language), check_word_str, 'Computers & Electronics, Javascript Language'))
        nlp_title_list.append((check_word.similarity(computers_laptops_computers), check_word_str, 'Computers & Electronics, Laptops Computers'))
        nlp_title_list.append((check_word.similarity(computers_linux), check_word_str, 'Computers & Electronics, Linux'))
        nlp_title_list.append((check_word.similarity(computers_mac), check_word_str, 'Computers & Electronics, MAC Computers'))
        nlp_title_list.append((check_word.similarity(computers_mac), check_word_str, 'Computers & Electronics, Mac Apple Computers'))
        nlp_title_list.append((check_word.similarity(computers_marketing_software), check_word_str, 'Computers & Electronics, Marketing Software'))
        nlp_title_list.append((check_word.similarity(computers_microsoft), check_word_str, 'Computers & Electronics, Microsoft'))
        nlp_title_list.append((check_word.similarity(computers_microsoft_windows), check_word_str, 'Computers & Electronics, Microsoft Windows'))
        nlp_title_list.append((check_word.similarity(computers_multimedia_software), check_word_str, 'Computers & Electronics, Multimedia Software'))
        nlp_title_list.append((check_word.similarity(computers_music_software), check_word_str, 'Computers & Electronics, Music Software'))
        nlp_title_list.append((check_word.similarity(computers_network_monitoring), check_word_str, 'Computers & Electronics, Network Monitoring'))
        nlp_title_list.append((check_word.similarity(computers_networking_data_formats), check_word_str, 'Computers & Electronics, Networking Data Formats'))
        nlp_title_list.append((check_word.similarity(computers_operating_systems), check_word_str, 'Computers & Electronics, Operating Systems'))
        nlp_title_list.append((check_word.similarity(computers_pc), check_word_str, 'Computers & Electronics, PC'))
        nlp_title_list.append((check_word.similarity(computers_php_language), check_word_str, 'Computers & Electronics, PHP'))
        nlp_title_list.append((check_word.similarity(computers_power_supplies), check_word_str, 'Computers & Electronics, Power Supplies'))
        nlp_title_list.append((check_word.similarity(computers_proxies), check_word_str, 'Computers & Electronics, Proxies'))
        nlp_title_list.append((check_word.similarity(computers_python_language), check_word_str, 'Computers & Electronics, Python Language'))
        nlp_title_list.append((check_word.similarity(computers_rc_aircraft), check_word_str, 'Computers & Electronics, Rc Aircraft'))
        nlp_title_list.append((check_word.similarity(computers_ruby_language), check_word_str, 'Computers & Electronics, Ruby Language'))
        nlp_title_list.append((check_word.similarity(computers_rust_language), check_word_str, 'Computers & Electronics, Rust Language'))
        nlp_title_list.append((check_word.similarity(computers_scala_language), check_word_str, 'Computers & Electronics, Scala Language'))
        nlp_title_list.append((check_word.similarity(computers_sd_card), check_word_str, 'Computers & Electronics, SD Secure Digital Cards'))
        nlp_title_list.append((check_word.similarity(computers_seo_software), check_word_str, 'Computers & Electronics, SEO Software'))
        nlp_title_list.append((check_word.similarity(computers_software_cracking), check_word_str, 'Computers & Electronics, Software Cracking'))
        nlp_title_list.append((check_word.similarity(computers_software_device_drivers), check_word_str, 'Computers & Electronics, Software Device Drivers'))
        nlp_title_list.append((check_word.similarity(computers_ssd), check_word_str, 'Computers & Electronics, SSD Solid State Drives'))
        nlp_title_list.append((check_word.similarity(computers_swift_language), check_word_str, 'Computers & Electronics, Swift Language'))
        nlp_title_list.append((check_word.similarity(computers_torrent), check_word_str, 'Computers & Electronics, Torrenting'))
        nlp_title_list.append((check_word.similarity(computers_torrent_software), check_word_str, 'Computers & Electronics, Torrent Software'))
        nlp_title_list.append((check_word.similarity(computers_utilities_software), check_word_str, 'Computers & Electronics, Utilities Software'))
        nlp_title_list.append((check_word.similarity(computers_video_equipment), check_word_str, 'Computers & Electronics, Video Equipment'))
        nlp_title_list.append((check_word.similarity(computers_video_software), check_word_str, 'Computers & Electronics, Video Software'))
        nlp_title_list.append((check_word.similarity(computers_virtual_reality), check_word_str, 'Computers & Electronics, Virtual Reality'))
        nlp_title_list.append((check_word.similarity(computers_vpns), check_word_str, 'Computers & Electronics, Vpns'))
        nlp_title_list.append((check_word.similarity(computers_wifi), check_word_str, 'Computers & Electronics, WiFi'))
        nlp_title_list.append((check_word.similarity(finance_accounting), check_word_str, 'Finance & Money, Accounting'))
        nlp_title_list.append((check_word.similarity(finance_auditing), check_word_str, 'Finance & Money, Auditing'))
        nlp_title_list.append((check_word.similarity(finance_auto_insurance), check_word_str, 'Finance & Money, Auto Insurance'))
        nlp_title_list.append((check_word.similarity(finance_banking), check_word_str, 'Finance & Money, Banking'))
        nlp_title_list.append((check_word.similarity(finance_benefits), check_word_str, 'Finance & Money, Financial Benefits'))
        nlp_title_list.append((check_word.similarity(finance_billing), check_word_str, 'Finance & Money, Billing'))
        nlp_title_list.append((check_word.similarity(finance_boat_insurance), check_word_str, 'Finance & Money, Boat Insurance'))
        nlp_title_list.append((check_word.similarity(finance_car_finance), check_word_str, 'Finance & Money, Auto Financing'))
        nlp_title_list.append((check_word.similarity(finance_commodities_trading), check_word_str, 'Finance & Money, Commodities Trading'))
        nlp_title_list.append((check_word.similarity(finance_credit), check_word_str, 'Finance & Money, Credit'))
        nlp_title_list.append((check_word.similarity(finance_credit_cards), check_word_str, 'Finance & Money, Credit Cards'))
        nlp_title_list.append((check_word.similarity(finance_credit_monitoring), check_word_str, 'Finance & Money, Credit Monitoring'))
        nlp_title_list.append((check_word.similarity(finance_credit_reporting), check_word_str, 'Finance & Money, Credit Reporting'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies), check_word_str, 'Finance & Money, Cryptocurrencies'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_binance_coin), check_word_str, 'Finance & Money, Cryptocurrencies Binance Coin'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_bitcoin), check_word_str, 'Finance & Money, Cryptocurrencies Bitcoin'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_bitcoin_cash), check_word_str, 'Finance & Money, Cryptocurrencies Bitcoin Cash'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_cardano), check_word_str, 'Finance & Money, Cryptocurrencies Cardano'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_chainlink), check_word_str, 'Finance & Money, Cryptocurrencies Chainlink'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_dash), check_word_str, 'Finance & Money, Cryptocurrencies Dash'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_dogecoin), check_word_str, 'Finance & Money, Cryptocurrencies Dogecoin'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_ethereum), check_word_str, 'Finance & Money, Cryptocurrencies Ethereum'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_litecoin), check_word_str, 'Finance & Money, Cryptocurrencies Litecoin'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_monero), check_word_str, 'Finance & Money, Cryptocurrencies Monero'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_nxt), check_word_str, 'Finance & Money, Cryptocurrencies Nxt'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_peercoin), check_word_str, 'Finance & Money, Cryptocurrencies Peercoin'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_polkadot), check_word_str, 'Finance & Money, Cryptocurrencies Polkadot'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_stellar), check_word_str, 'Finance & Money, Cryptocurrencies Stellar'))
        nlp_title_list.append((check_word.similarity(finance_cryptocurrencies_tether), check_word_str, 'Finance & Money, Cryptocurrencies Tether'))
        nlp_title_list.append((check_word.similarity(finance_finance), check_word_str, 'Finance & Money, Finance'))
        nlp_title_list.append((check_word.similarity(finance_finance_grants), check_word_str, 'Finance & Money, Finance Grants'))
        nlp_title_list.append((check_word.similarity(finance_finance_investing), check_word_str, 'Finance & Money, Finance Investing'))
        nlp_title_list.append((check_word.similarity(finance_finance_scholarships), check_word_str, 'Finance & Money, Finance Scholarships'))
        nlp_title_list.append((check_word.similarity(finance_financial_aid), check_word_str, 'Finance & Money, Financial Aid'))
        nlp_title_list.append((check_word.similarity(finance_financial_planning), check_word_str, 'Finance & Money, Financial Planning'))
        nlp_title_list.append((check_word.similarity(finance_futures_trading), check_word_str, 'Finance & Money, Futures Trading'))
        nlp_title_list.append((check_word.similarity(finance_health_insurance), check_word_str, 'Finance & Money, Health Insurance'))
        nlp_title_list.append((check_word.similarity(finance_home_insurance), check_word_str, 'Finance & Money, Home Insurance'))
        nlp_title_list.append((check_word.similarity(finance_insurance), check_word_str, 'Finance & Money, Insurance'))
        nlp_title_list.append((check_word.similarity(finance_invest_home), check_word_str, 'Finance & Money, Home Investing'))
        nlp_title_list.append((check_word.similarity(finance_investing_bonds), check_word_str, 'Finance & Money, Investing Bonds'))
        nlp_title_list.append((check_word.similarity(finance_investing_currencies), check_word_str, 'Finance & Money, Investing Currencies'))
        nlp_title_list.append((check_word.similarity(finance_investing_gold), check_word_str, 'Finance & Money, Investing Gold'))
        nlp_title_list.append((check_word.similarity(finance_investing_oil), check_word_str, 'Finance & Money, Investing Oil'))
        nlp_title_list.append((check_word.similarity(finance_investing_precious_metals), check_word_str, 'Finance & Money, Investing Precious Metals'))
        nlp_title_list.append((check_word.similarity(finance_investing_silver), check_word_str, 'Finance & Money, Investing Silver'))
        nlp_title_list.append((check_word.similarity(finance_investing_stocks), check_word_str, 'Finance & Money, Investing Stocks'))
        nlp_title_list.append((check_word.similarity(finance_invoicing), check_word_str, 'Finance & Money, Invoicing'))
        nlp_title_list.append((check_word.similarity(finance_lending), check_word_str, 'Finance & Money, Lending'))
        nlp_title_list.append((check_word.similarity(finance_life_insurance), check_word_str, 'Finance & Money, Life Insurance'))
        nlp_title_list.append((check_word.similarity(finance_loans), check_word_str, 'Finance & Money, Loans'))
        nlp_title_list.append((check_word.similarity(finance_retirement_pension), check_word_str, 'Finance & Money, Retirement Pension'))
        nlp_title_list.append((check_word.similarity(finance_retirement_planning), check_word_str, 'Finance & Money, Retirement Planning'))
        nlp_title_list.append((check_word.similarity(finance_stocks), check_word_str, 'Finance & Money, Stocks'))
        nlp_title_list.append((check_word.similarity(finance_tax_preparation), check_word_str, 'Finance & Money, Tax Preparation'))
        nlp_title_list.append((check_word.similarity(finance_taxes), check_word_str, 'Finance & Money, Taxation'))
        nlp_title_list.append((check_word.similarity(finance_wealth), check_word_str, 'Finance & Money, Financial Wealth'))
        nlp_title_list.append((check_word.similarity(food_baked_goods), check_word_str, 'Food & Drink, Baked Goods'))
        nlp_title_list.append((check_word.similarity(food_bbq_cooking), check_word_str, 'Food & Drink, Bbq Cooking'))
        nlp_title_list.append((check_word.similarity(food_bbq_recipes), check_word_str, 'Food & Drink, Bbq Recipes'))
        nlp_title_list.append((check_word.similarity(food_beer), check_word_str, 'Food & Drink, Beer'))
        nlp_title_list.append((check_word.similarity(food_beverage_drinks), check_word_str, 'Food & Drink, Beverage Drinks'))
        nlp_title_list.append((check_word.similarity(food_breakfast_foods), check_word_str, 'Food & Drink, Breakfast Foods'))
        nlp_title_list.append((check_word.similarity(food_candy), check_word_str, 'Food & Drink, Candy'))
        nlp_title_list.append((check_word.similarity(food_coffee), check_word_str, 'Food & Drink, Coffee'))
        nlp_title_list.append((check_word.similarity(food_cooking_recipes), check_word_str, 'Food & Drink, Cooking Recipes'))
        nlp_title_list.append((check_word.similarity(food_dessert_recipes), check_word_str, 'Food & Drink, Dessert Recipes'))
        nlp_title_list.append((check_word.similarity(food_drink), check_word_str, 'Food & Drink, Drink'))
        nlp_title_list.append((check_word.similarity(food_fast_food), check_word_str, 'Food & Drink, Fast Food'))
        nlp_title_list.append((check_word.similarity(food_food), check_word_str, 'Food & Drink, Food'))
        nlp_title_list.append((check_word.similarity(food_food_cooking), check_word_str, 'Food & Drink, Food Cooking'))
        nlp_title_list.append((check_word.similarity(food_food_grains), check_word_str, 'Food & Drink, Food Grains'))
        nlp_title_list.append((check_word.similarity(food_fruits), check_word_str, 'Food & Drink, Fruits'))
        nlp_title_list.append((check_word.similarity(food_grill_cooking), check_word_str, 'Food & Drink, Grill Cooking'))
        nlp_title_list.append((check_word.similarity(food_grill_recipes), check_word_str, 'Food & Drink, Grill Recipes'))
        nlp_title_list.append((check_word.similarity(food_grocery_retailers), check_word_str, 'Food & Drink, Grocery Retailers'))
        nlp_title_list.append((check_word.similarity(food_grocery_stores), check_word_str, 'Food & Drink, Grocery Stores'))
        nlp_title_list.append((check_word.similarity(food_juice_beverages), check_word_str, 'Food & Drink, Juice Beverages'))
        nlp_title_list.append((check_word.similarity(food_liquor), check_word_str, 'Food & Drink, Liquor'))
        nlp_title_list.append((check_word.similarity(food_meat_foods), check_word_str, 'Food & Drink, Meat Foods'))
        nlp_title_list.append((check_word.similarity(food_pasta), check_word_str, 'Food & Drink, Pasta'))
        nlp_title_list.append((check_word.similarity(food_pizzerias), check_word_str, 'Food & Drink, Pizzerias'))
        nlp_title_list.append((check_word.similarity(food_restaurant_reservations), check_word_str, 'Food & Drink, Restaurant Reservations'))
        nlp_title_list.append((check_word.similarity(food_restaurant_reviews), check_word_str, 'Food & Drink, Restaurant Reviews'))
        nlp_title_list.append((check_word.similarity(food_restaurants), check_word_str, 'Food & Drink, Restaurants'))
        nlp_title_list.append((check_word.similarity(food_seafood), check_word_str, 'Food & Drink, Seafood'))
        nlp_title_list.append((check_word.similarity(food_snack_foods), check_word_str, 'Food & Drink, Snack Foods'))
        nlp_title_list.append((check_word.similarity(food_soft_drinks), check_word_str, 'Food & Drink, Soft Drinks'))
        nlp_title_list.append((check_word.similarity(food_soup_recipes), check_word_str, 'Food & Drink, Soup Recipes'))
        nlp_title_list.append((check_word.similarity(food_spirit_alcohol), check_word_str, 'Food & Drink, Spirit Alcohol'))
        nlp_title_list.append((check_word.similarity(food_stew_recipes), check_word_str, 'Food & Drink, Stew Recipes'))
        nlp_title_list.append((check_word.similarity(food_sweets), check_word_str, 'Food & Drink, Sweets'))
        nlp_title_list.append((check_word.similarity(food_tea), check_word_str, 'Food & Drink, Tea'))
        nlp_title_list.append((check_word.similarity(food_vegetables), check_word_str, 'Food & Drink, Vegetables'))
        nlp_title_list.append((check_word.similarity(food_wine), check_word_str, 'Food & Drink, Wine'))
        nlp_title_list.append((check_word.similarity(games_arcade_games), check_word_str, 'Games, Arcade Games'))
        nlp_title_list.append((check_word.similarity(games_billiards_games), check_word_str, 'Games, Billiards Games'))
        nlp_title_list.append((check_word.similarity(games_blackjack_games), check_word_str, 'Games, Blackjack Games'))
        nlp_title_list.append((check_word.similarity(games_board_games), check_word_str, 'Games, Board Games'))
        nlp_title_list.append((check_word.similarity(games_brainteasers), check_word_str, 'Games, Brainteasers'))
        nlp_title_list.append((check_word.similarity(games_card_games), check_word_str, 'Games, Card Games'))
        nlp_title_list.append((check_word.similarity(games_casino_games), check_word_str, 'Games, Casino Games'))
        nlp_title_list.append((check_word.similarity(games_casual_video_games), check_word_str, 'Games, Casual Video Games'))
        nlp_title_list.append((check_word.similarity(games_checkers_games), check_word_str, 'Games, Checkers Games'))
        nlp_title_list.append((check_word.similarity(games_chess_game), check_word_str, 'Games, Chess Game'))
        nlp_title_list.append((check_word.similarity(games_collectible_card_games), check_word_str, 'Games, Collectible Card Games'))
        nlp_title_list.append((check_word.similarity(games_collectible_cards), check_word_str, 'Games, Collectible Cards'))
        nlp_title_list.append((check_word.similarity(games_coloring), check_word_str, 'Games, Coloring'))
        nlp_title_list.append((check_word.similarity(games_drawing), check_word_str, 'Games, Drawing'))
        nlp_title_list.append((check_word.similarity(games_dress_up_games), check_word_str, 'Games, Dress Up Games'))
        nlp_title_list.append((check_word.similarity(games_family_drawing_coloring), check_word_str, 'Games, Family Drawing Coloring'))
        nlp_title_list.append((check_word.similarity(games_family_dress_up_games), check_word_str, 'Games, Family Dress Up Games'))
        nlp_title_list.append((check_word.similarity(games_family_games), check_word_str, 'Games, Family Games'))
        nlp_title_list.append((check_word.similarity(games_gambling), check_word_str, 'Games, Gambling'))
        nlp_title_list.append((check_word.similarity(games_games), check_word_str, 'Games, Games'))
        nlp_title_list.append((check_word.similarity(games_lottery), check_word_str, 'Games, Lottery'))
        nlp_title_list.append((check_word.similarity(games_online_massively_multiplayer_games), check_word_str, 'Games, Online Massively Multiplayer Games'))
        nlp_title_list.append((check_word.similarity(games_poker_games), check_word_str, 'Games, Poker Games'))
        nlp_title_list.append((check_word.similarity(games_puzzles), check_word_str, 'Games, Puzzles'))
        nlp_title_list.append((check_word.similarity(games_roleplaying_games), check_word_str, 'Games, Roleplaying Games'))
        nlp_title_list.append((check_word.similarity(games_strategy_games), check_word_str, 'Games, Strategy Games'))
        nlp_title_list.append((check_word.similarity(games_table_games), check_word_str, 'Games, Table Games'))
        nlp_title_list.append((check_word.similarity(games_video_dance_games), check_word_str, 'Games, Video Dance Games'))
        nlp_title_list.append((check_word.similarity(games_video_driving_games), check_word_str, 'Games, Video Driving Games'))
        nlp_title_list.append((check_word.similarity(games_video_fighting_games), check_word_str, 'Games, Video Fighting Games'))
        nlp_title_list.append((check_word.similarity(games_video_flying_games), check_word_str, 'Games, Video Flying Games'))
        nlp_title_list.append((check_word.similarity(games_video_game_emulation), check_word_str, 'Games, Video Game Emulation'))
        nlp_title_list.append((check_word.similarity(games_video_games), check_word_str, 'Games, Video Games'))
        nlp_title_list.append((check_word.similarity(games_video_puzzle_games), check_word_str, 'Games, Video Puzzle Games'))
        nlp_title_list.append((check_word.similarity(games_video_racing_games), check_word_str, 'Games, Video Racing Games'))
        nlp_title_list.append((check_word.similarity(games_video_sandbox_games), check_word_str, 'Games, Video Sandbox Games'))
        nlp_title_list.append((check_word.similarity(games_video_shooter_games), check_word_str, 'Games, Video Shooter Games'))
        nlp_title_list.append((check_word.similarity(games_video_simulation_games), check_word_str, 'Games, Video Simulation Games'))
        nlp_title_list.append((check_word.similarity(games_video_sports_games), check_word_str, 'Games, Video Sports Games'))
        nlp_title_list.append((check_word.similarity(games_video_strategy_games), check_word_str, 'Games, Video Strategy Games'))
        nlp_title_list.append((check_word.similarity(games_video_war_games), check_word_str, 'Games, Video War Games'))
        nlp_title_list.append((check_word.similarity(games_video_word_games), check_word_str, 'Games, Video Word Games'))
        nlp_title_list.append((check_word.similarity(games_war_games), check_word_str, 'Games, War Games'))
        nlp_title_list.append((check_word.similarity(games_word_games), check_word_str, 'Games, Word Games'))
        nlp_title_list.append((check_word.similarity(general_accidents), check_word_str, 'Accidents, General Accidents'))
        nlp_title_list.append((check_word.similarity(general_advice), check_word_str, 'Advice, General Advice'))
        nlp_title_list.append((check_word.similarity(general_agreements), check_word_str, 'Agreements, General Agreements'))
        nlp_title_list.append((check_word.similarity(general_air_force), check_word_str, 'Air Force, General Air Force'))
        nlp_title_list.append((check_word.similarity(general_alternative_energy), check_word_str, 'General Alternative Energy'))
        nlp_title_list.append((check_word.similarity(general_answers), check_word_str, 'Answers, General Answers'))
        nlp_title_list.append((check_word.similarity(general_arguments), check_word_str, 'Arguments, General Arguments'))
        nlp_title_list.append((check_word.similarity(general_army), check_word_str, 'Army, General Army'))
        nlp_title_list.append((check_word.similarity(general_assistance), check_word_str, 'Assistance, General Assistance'))
        nlp_title_list.append((check_word.similarity(general_awareness), check_word_str, 'Awareness, General Awareness'))
        nlp_title_list.append((check_word.similarity(general_celebrations), check_word_str, 'Celebrations, General Celebrations'))
        nlp_title_list.append((check_word.similarity(general_coast_guard), check_word_str, 'Coast Guar, General Coast Guard'))
        nlp_title_list.append((check_word.similarity(general_competition), check_word_str, 'Competition, General Competition'))
        nlp_title_list.append((check_word.similarity(general_complaints), check_word_str, 'Complaints, General Complaints'))
        nlp_title_list.append((check_word.similarity(general_confusion), check_word_str, 'Confusion, General Confusion'))
        nlp_title_list.append((check_word.similarity(general_consequence), check_word_str, 'Consequences, General Consequences'))
        nlp_title_list.append((check_word.similarity(general_conservation), check_word_str, 'Conservation, General Conservation'))
        nlp_title_list.append((check_word.similarity(general_courage), check_word_str, 'Courage, General Courage'))
        nlp_title_list.append((check_word.similarity(general_criticism), check_word_str, 'Criticism, General Criticism'))
        nlp_title_list.append((check_word.similarity(general_death), check_word_str, 'Death, General Death'))
        nlp_title_list.append((check_word.similarity(general_disorder), check_word_str, 'Disorder, General Disorder'))
        nlp_title_list.append((check_word.similarity(general_efficiency), check_word_str, 'Efficiency, General Efficiency'))
        nlp_title_list.append((check_word.similarity(general_emergencies), check_word_str, 'Emergencies, General Emergencies'))
        nlp_title_list.append((check_word.similarity(general_emotions), check_word_str, 'Emotions, General Emotions'))
        nlp_title_list.append((check_word.similarity(general_energy), check_word_str, 'Energy, General Energy'))
        nlp_title_list.append((check_word.similarity(general_enthusiasm), check_word_str, 'Enthusiasm, General Enthusiasm'))
        nlp_title_list.append((check_word.similarity(general_equipment), check_word_str, 'Equipment, General Equipment'))
        nlp_title_list.append((check_word.similarity(general_excitement), check_word_str, 'Excitement, General Excitement'))
        nlp_title_list.append((check_word.similarity(general_extermination), check_word_str, 'Extermination, General Extermination'))
        nlp_title_list.append((check_word.similarity(general_feedback), check_word_str, 'Feedback, General Feedback'))
        nlp_title_list.append((check_word.similarity(general_fortune), check_word_str, 'Fortunes, General Fortunes'))
        nlp_title_list.append((check_word.similarity(general_fun), check_word_str, 'Fun, General Fun'))
        nlp_title_list.append((check_word.similarity(general_growth), check_word_str, 'Growth, General Growth'))
        nlp_title_list.append((check_word.similarity(general_guide), check_word_str, 'Guides, General Guides'))
        nlp_title_list.append((check_word.similarity(general_homework), check_word_str, 'Homework, General Homework'))
        nlp_title_list.append((check_word.similarity(general_hope), check_word_str, 'Hope, General Hope'))
        nlp_title_list.append((check_word.similarity(general_improvement), check_word_str, 'Improvement, General Improvement'))
        nlp_title_list.append((check_word.similarity(general_information), check_word_str, 'Information, General Information'))
        nlp_title_list.append((check_word.similarity(general_instruction), check_word_str, 'Instruction, General Instruction'))
        nlp_title_list.append((check_word.similarity(general_interest), check_word_str, 'Interests, General Interests'))
        nlp_title_list.append((check_word.similarity(general_issues), check_word_str, 'Issues, General Issues'))
        nlp_title_list.append((check_word.similarity(general_luck), check_word_str, 'Luck, General Luck'))
        nlp_title_list.append((check_word.similarity(general_maintenance), check_word_str, 'Maintenance, General Maintenance'))
        nlp_title_list.append((check_word.similarity(general_management), check_word_str, 'Management, General Management'))
        nlp_title_list.append((check_word.similarity(general_marines), check_word_str, 'Marines, General Marines'))
        nlp_title_list.append((check_word.similarity(general_masonry), check_word_str, 'Masonry, General Masonry'))
        nlp_title_list.append((check_word.similarity(general_memberships), check_word_str, 'Membership, General Membership'))
        nlp_title_list.append((check_word.similarity(general_military), check_word_str, 'Military, General Military'))
        nlp_title_list.append((check_word.similarity(general_mind), check_word_str, 'Mind, General Mind'))
        nlp_title_list.append((check_word.similarity(general_navy), check_word_str, 'Navy, General Navy'))
        nlp_title_list.append((check_word.similarity(general_networking), check_word_str, 'Networking, General Networking'))
        nlp_title_list.append((check_word.similarity(general_opinion), check_word_str, 'Opinion, General Opinion'))
        nlp_title_list.append((check_word.similarity(general_panic), check_word_str, 'Panic, General Panic'))
        nlp_title_list.append((check_word.similarity(general_perception), check_word_str, 'Perception, General Perception'))
        nlp_title_list.append((check_word.similarity(general_perspective), check_word_str, 'Perspective, General Perspective'))
        nlp_title_list.append((check_word.similarity(general_philosophy), check_word_str, 'Philosophy, General Philosophy'))
        nlp_title_list.append((check_word.similarity(general_pollution), check_word_str, 'Pollution, General Pollution'))
        nlp_title_list.append((check_word.similarity(general_problems), check_word_str, 'Problems, General Problems'))
        nlp_title_list.append((check_word.similarity(general_progress), check_word_str, 'Progress, General Progress'))
        nlp_title_list.append((check_word.similarity(general_purpose), check_word_str, 'Purpose, General Purpose'))
        nlp_title_list.append((check_word.similarity(general_questions), check_word_str, 'Questions, General Questions'))
        nlp_title_list.append((check_word.similarity(general_recommendations), check_word_str, 'Recommendations, General Recommendations'))
        nlp_title_list.append((check_word.similarity(general_repair), check_word_str, 'Repair, General Repair'))
        nlp_title_list.append((check_word.similarity(general_requirements), check_word_str, 'Requirements, General Requirements'))
        nlp_title_list.append((check_word.similarity(general_research), check_word_str, 'Research, General Research'))
        nlp_title_list.append((check_word.similarity(general_reviews), check_word_str, 'Reviews, General Reviews'))
        nlp_title_list.append((check_word.similarity(general_risk), check_word_str, 'Risk, General Risk'))
        nlp_title_list.append((check_word.similarity(general_schools), check_word_str, 'Schools, General Schools'))
        nlp_title_list.append((check_word.similarity(general_service), check_word_str, 'Service, General Service'))
        nlp_title_list.append((check_word.similarity(general_solutions), check_word_str, 'Solutions, General Solutions'))
        nlp_title_list.append((check_word.similarity(general_space_force), check_word_str, 'Space Force, General Space Force'))
        nlp_title_list.append((check_word.similarity(general_storage), check_word_str, 'Storage, General Storage'))
        nlp_title_list.append((check_word.similarity(general_success), check_word_str, 'Success, General Success'))
        nlp_title_list.append((check_word.similarity(general_theories), check_word_str, 'Theories, General Theories'))
        nlp_title_list.append((check_word.similarity(general_tools), check_word_str, 'Tools, General Tools'))
        nlp_title_list.append((check_word.similarity(general_training), check_word_str, 'Training, General Training'))
        nlp_title_list.append((check_word.similarity(general_trouble), check_word_str, 'Trouble, General Trouble'))
        nlp_title_list.append((check_word.similarity(general_utilities), check_word_str, 'Utilities, General Utilities'))
        nlp_title_list.append((check_word.similarity(general_warning), check_word_str, 'Warning, General Warning'))
        nlp_title_list.append((check_word.similarity(health_aids), check_word_str, 'Health, Aids'))
        nlp_title_list.append((check_word.similarity(health_alcohol_testing), check_word_str, 'Health, Alcohol Testing'))
        nlp_title_list.append((check_word.similarity(health_alcohol_treatment), check_word_str, 'Health, Alcohol Treatment'))
        nlp_title_list.append((check_word.similarity(health_allergies), check_word_str, 'Health, Allergies'))
        nlp_title_list.append((check_word.similarity(health_anxiety), check_word_str, 'Health, Anxiety'))
        nlp_title_list.append((check_word.similarity(health_arthritis), check_word_str, 'Health, Arthritis'))
        nlp_title_list.append((check_word.similarity(health_assisted_living), check_word_str, 'Health, Assisted Living'))
        nlp_title_list.append((check_word.similarity(health_cancer), check_word_str, 'Health, Cancer'))
        nlp_title_list.append((check_word.similarity(health_conditions_ear), check_word_str, 'Health, Conditions Ear'))
        nlp_title_list.append((check_word.similarity(health_conditions_ear_nose_throat), check_word_str, 'Health, Conditions Ear Nose Throat'))
        nlp_title_list.append((check_word.similarity(health_conditions_ethroat), check_word_str, 'Health, Conditions Ethroat'))
        nlp_title_list.append((check_word.similarity(health_conditions_nose), check_word_str, 'Health, Conditions Nose'))
        nlp_title_list.append((check_word.similarity(health_contacts), check_word_str, 'Health, Contacts'))
        nlp_title_list.append((check_word.similarity(health_covid), check_word_str, 'Health, Covid'))
        nlp_title_list.append((check_word.similarity(health_dental_care), check_word_str, 'Health, Dental Care'))
        nlp_title_list.append((check_word.similarity(health_depression), check_word_str, 'Health, Depression'))
        nlp_title_list.append((check_word.similarity(health_diabetes), check_word_str, 'Health, Diabetes'))
        nlp_title_list.append((check_word.similarity(health_diets), check_word_str, 'Health, Diets'))
        nlp_title_list.append((check_word.similarity(health_disabilities), check_word_str, 'Health, Disabilities'))
        nlp_title_list.append((check_word.similarity(health_diseases), check_word_str, 'Health, Diseases'))
        nlp_title_list.append((check_word.similarity(health_doctors_offices), check_word_str, 'Health, Doctors Offices'))
        nlp_title_list.append((check_word.similarity(health_drug_testing), check_word_str, 'Health, Drug Testing'))
        nlp_title_list.append((check_word.similarity(health_drug_treatment), check_word_str, 'Health, Drug Treatment'))
        nlp_title_list.append((check_word.similarity(health_eating_disorders), check_word_str, 'Health, Eating Disorders'))
        nlp_title_list.append((check_word.similarity(health_endocrine_conditions), check_word_str, 'Health, Endocrine Conditions'))
        nlp_title_list.append((check_word.similarity(health_eyeglasses), check_word_str, 'Health, Eyeglasses'))
        nlp_title_list.append((check_word.similarity(health_genes), check_word_str, 'Health, Genes'))
        nlp_title_list.append((check_word.similarity(health_genetic_disorders), check_word_str, 'Health, Genetic Disorders'))
        nlp_title_list.append((check_word.similarity(health_health), check_word_str, 'Health, Health'))
        nlp_title_list.append((check_word.similarity(health_health_aging), check_word_str, 'Health, Health Aging'))
        nlp_title_list.append((check_word.similarity(health_health_conditions), check_word_str, 'Health, Health Conditions'))
        nlp_title_list.append((check_word.similarity(health_health_pharmacy), check_word_str, 'Health, Health Pharmacy'))
        nlp_title_list.append((check_word.similarity(health_health_quit_smoking), check_word_str, 'Health, Health Quit Smoking'))
        nlp_title_list.append((check_word.similarity(health_health_records), check_word_str, 'Health, Health Records'))
        nlp_title_list.append((check_word.similarity(health_heart_conditions), check_word_str, 'Health, Heart Conditions'))
        nlp_title_list.append((check_word.similarity(health_hiv), check_word_str, 'Health, HIV'))
        nlp_title_list.append((check_word.similarity(health_homeopathy), check_word_str, 'Health, Homeopathy'))
        nlp_title_list.append((check_word.similarity(health_hospitals), check_word_str, 'Health, Hospitals'))
        nlp_title_list.append((check_word.similarity(health_hypertension), check_word_str, 'Health, Hypertension'))
        nlp_title_list.append((check_word.similarity(health_immune_system), check_word_str, 'Health, Immune System'))
        nlp_title_list.append((check_word.similarity(health_infectious_diseases), check_word_str, 'Health, Infectious Diseases'))
        nlp_title_list.append((check_word.similarity(health_injury), check_word_str, 'Health, Injury'))
        nlp_title_list.append((check_word.similarity(health_medical_devices), check_word_str, 'Health, Medical Devices'))
        nlp_title_list.append((check_word.similarity(health_medical_equipment), check_word_str, 'Health, Medical Equipment'))
        nlp_title_list.append((check_word.similarity(health_medical_facilities), check_word_str, 'Health, Medical Facilities'))
        nlp_title_list.append((check_word.similarity(health_medical_procedures), check_word_str, 'Health, Medical Procedures'))
        nlp_title_list.append((check_word.similarity(health_medical_research), check_word_str, 'Health, Medical Research'))
        nlp_title_list.append((check_word.similarity(health_medical_services), check_word_str, 'Health, Medical Services'))
        nlp_title_list.append((check_word.similarity(health_medical_training), check_word_str, 'Health, Medical Training'))
        nlp_title_list.append((check_word.similarity(health_medications), check_word_str, 'Health, Medications'))
        nlp_title_list.append((check_word.similarity(health_medicine), check_word_str, 'Health, Medicine'))
        nlp_title_list.append((check_word.similarity(health_meditation), check_word_str, 'Health, Meditation'))
        nlp_title_list.append((check_word.similarity(health_men_health), check_word_str, 'Health, Men Health'))
        nlp_title_list.append((check_word.similarity(health_mental_health), check_word_str, 'Health, Mental Health'))
        nlp_title_list.append((check_word.similarity(health_mental_therapy), check_word_str, 'Health, Mental Therapies'))
        nlp_title_list.append((check_word.similarity(health_neurological_conditions), check_word_str, 'Health, Neurological Conditions'))
        nlp_title_list.append((check_word.similarity(health_nursing_service), check_word_str, 'Health, Nursing Service'))
        nlp_title_list.append((check_word.similarity(health_nutrition), check_word_str, 'Health, Nutrition'))
        nlp_title_list.append((check_word.similarity(health_nutrition_supplements), check_word_str, 'Health, Nutrition Supplements'))
        nlp_title_list.append((check_word.similarity(health_obesity), check_word_str, 'Health, Obesity'))
        nlp_title_list.append((check_word.similarity(health_occupational_health), check_word_str, 'Health, Occupational Health'))
        nlp_title_list.append((check_word.similarity(health_occupational_safety), check_word_str, 'Health, Occupational Safety'))
        nlp_title_list.append((check_word.similarity(health_oral_care), check_word_str, 'Health, Oral Care'))
        nlp_title_list.append((check_word.similarity(health_pain_management), check_word_str, 'Health, Pain Management'))
        nlp_title_list.append((check_word.similarity(health_physical_therapy), check_word_str, 'Health, Physical Therapy'))
        nlp_title_list.append((check_word.similarity(health_public_health), check_word_str, 'Health, Public Health'))
        nlp_title_list.append((check_word.similarity(health_reproductive_health), check_word_str, 'Health, Reproductive Health'))
        nlp_title_list.append((check_word.similarity(health_respiratory_conditions), check_word_str, 'Health, Respiratory Conditions'))
        nlp_title_list.append((check_word.similarity(health_restricted_diets), check_word_str, 'Health, Restricted Diets'))
        nlp_title_list.append((check_word.similarity(health_skin_conditions), check_word_str, 'Health, Skin Conditions'))
        nlp_title_list.append((check_word.similarity(health_sleep_disorders), check_word_str, 'Health, Sleep Disorders'))
        nlp_title_list.append((check_word.similarity(health_special_diets), check_word_str, 'Health, Special Diets'))
        nlp_title_list.append((check_word.similarity(health_sports_injury), check_word_str, 'Health, Sports Injury'))
        nlp_title_list.append((check_word.similarity(health_steroids_abuse), check_word_str, 'Health, Steroids Abuse'))
        nlp_title_list.append((check_word.similarity(health_stress), check_word_str, 'Health, Stress'))
        nlp_title_list.append((check_word.similarity(health_stroke), check_word_str, 'Health, Stroke'))
        nlp_title_list.append((check_word.similarity(health_substance_abuse), check_word_str, 'Health, Substance Abuse'))
        nlp_title_list.append((check_word.similarity(health_surgery), check_word_str, 'Health, Surgery'))
        nlp_title_list.append((check_word.similarity(health_symptoms), check_word_str, 'Health, Symptoms'))
        nlp_title_list.append((check_word.similarity(health_therapy), check_word_str, 'Health, Therapies'))
        nlp_title_list.append((check_word.similarity(health_trauma), check_word_str, 'Health, Mental Trauma'))
        nlp_title_list.append((check_word.similarity(health_treatment_centers), check_word_str, 'Health, Treatment Centers'))
        nlp_title_list.append((check_word.similarity(health_vision_care), check_word_str, 'Health, Vision Care'))
        nlp_title_list.append((check_word.similarity(health_vitamins_supplements), check_word_str, 'Health, Vitamins Supplements'))
        nlp_title_list.append((check_word.similarity(health_women_health), check_word_str, 'Health, Women Health'))
        nlp_title_list.append((check_word.similarity(hobbies_arts_crafts), check_word_str, 'Hobbies, Arts Crafts'))
        nlp_title_list.append((check_word.similarity(hobbies_boating), check_word_str, 'Hobbies, Boating'))
        nlp_title_list.append((check_word.similarity(hobbies_camping), check_word_str, 'Hobbies, Camping'))
        nlp_title_list.append((check_word.similarity(hobbies_clubs), check_word_str, 'Hobbies, Clubs'))
        nlp_title_list.append((check_word.similarity(hobbies_contests), check_word_str, 'Hobbies, Contests'))
        nlp_title_list.append((check_word.similarity(hobbies_crafts), check_word_str, 'Hobbies, Crafts'))
        nlp_title_list.append((check_word.similarity(hobbies_fiber_crafts), check_word_str, 'Hobbies, Fiber Crafts'))
        nlp_title_list.append((check_word.similarity(hobbies_fishing), check_word_str, 'Hobbies, Fishing'))
        nlp_title_list.append((check_word.similarity(hobbies_hiking), check_word_str, 'Hobbies, Hiking'))
        nlp_title_list.append((check_word.similarity(hobbies_hobbies), check_word_str, 'Hobbies, Hobbies'))
        nlp_title_list.append((check_word.similarity(hobbies_leisure), check_word_str, 'Hobbies, Leisure'))
        nlp_title_list.append((check_word.similarity(hobbies_merit_prizes), check_word_str, 'Hobbies, Merit Prizes'))
        nlp_title_list.append((check_word.similarity(hobbies_model_railroads), check_word_str, 'Hobbies, Model Railroads'))
        nlp_title_list.append((check_word.similarity(hobbies_model_trains), check_word_str, 'Hobbies, Model Trains'))
        nlp_title_list.append((check_word.similarity(hobbies_modeling), check_word_str, 'Hobbies, Modeling'))
        nlp_title_list.append((check_word.similarity(hobbies_organizations), check_word_str, 'Hobbies, Organizations'))
        nlp_title_list.append((check_word.similarity(hobbies_outdoors), check_word_str, 'Hobbies, Outdoors'))
        nlp_title_list.append((check_word.similarity(hobbies_paintball), check_word_str, 'Hobbies, Paintball'))
        nlp_title_list.append((check_word.similarity(hobbies_radio_control), check_word_str, 'Hobbies, Radio Control'))
        nlp_title_list.append((check_word.similarity(hobbies_seasonal_events), check_word_str, 'Hobbies, Seasonal Events'))
        nlp_title_list.append((check_word.similarity(hobbies_special_holidays), check_word_str, 'Hobbies, Special Holidays'))
        nlp_title_list.append((check_word.similarity(hobbies_special_occasions), check_word_str, 'Hobbies, Special Occasions'))
        nlp_title_list.append((check_word.similarity(hobbies_surfing), check_word_str, 'Hobbies, Surfing'))
        nlp_title_list.append((check_word.similarity(hobbies_swimming), check_word_str, 'Hobbies, Swimming'))
        nlp_title_list.append((check_word.similarity(hobbies_textile_crafts), check_word_str, 'Hobbies, Textile Crafts'))
        nlp_title_list.append((check_word.similarity(hobbies_weddings), check_word_str, 'Wedding Events, Weddings'))
        nlp_title_list.append((check_word.similarity(hobbies_youth_clubs), check_word_str, 'Hobbies, Youth Clubs'))
        nlp_title_list.append((check_word.similarity(hobbies_youth_organizations), check_word_str, 'Hobbies, Youth Organizations'))
        nlp_title_list.append((check_word.similarity(hobbies_youth_resources), check_word_str, 'Hobbies, Youth Resources'))
        nlp_title_list.append((check_word.similarity(home_bed), check_word_str, 'Home & Garden, Bed'))
        nlp_title_list.append((check_word.similarity(home_curtains_treatments), check_word_str, 'Home & Garden, Curtains Treatments'))
        nlp_title_list.append((check_word.similarity(home_dining_furniture), check_word_str, 'Home & Garden, Dining Furniture'))
        nlp_title_list.append((check_word.similarity(home_domestic_services), check_word_str, 'Home & Garden, Domestic Services'))
        nlp_title_list.append((check_word.similarity(home_foundation), check_word_str, 'Home & Garden, Home Foundation'))
        nlp_title_list.append((check_word.similarity(home_garden), check_word_str, 'Home & Garden, Garden'))
        nlp_title_list.append((check_word.similarity(home_garden_pest_control), check_word_str, 'Home & Garden, Garden Pest Control'))
        nlp_title_list.append((check_word.similarity(home_home), check_word_str, 'Home & Garden, Home'))
        nlp_title_list.append((check_word.similarity(home_home_appliances), check_word_str, 'Home & Garden, Home Appliances'))
        nlp_title_list.append((check_word.similarity(home_home_carpets), check_word_str, 'Home & Garden, Home Carpets'))
        nlp_title_list.append((check_word.similarity(home_home_climate_control), check_word_str, 'Home & Garden, Home Climate Control'))
        nlp_title_list.append((check_word.similarity(home_home_cookware), check_word_str, 'Home & Garden, Home Cookware'))
        nlp_title_list.append((check_word.similarity(home_home_curtains), check_word_str, 'Home & Garden, Home Curtains'))
        nlp_title_list.append((check_word.similarity(home_home_decoration), check_word_str, 'Home & Garden, Home Decoration'))
        nlp_title_list.append((check_word.similarity(home_home_dining_room), check_word_str, 'Home & Garden, Home Dining Room'))
        nlp_title_list.append((check_word.similarity(home_home_diningware), check_word_str, 'Home & Garden, Home Diningware'))
        nlp_title_list.append((check_word.similarity(home_home_dryers), check_word_str, 'Home & Garden, Home Dryers'))
        nlp_title_list.append((check_word.similarity(home_home_fireplaces), check_word_str, 'Home & Garden, Home Fireplaces'))
        nlp_title_list.append((check_word.similarity(home_home_flooring), check_word_str, 'Home & Garden, Home Flooring'))
        nlp_title_list.append((check_word.similarity(home_home_furnishings), check_word_str, 'Home & Garden, Home Furnishings'))
        nlp_title_list.append((check_word.similarity(home_home_furniture), check_word_str, 'Home & Garden, Home Furniture'))
        nlp_title_list.append((check_word.similarity(home_home_garden), check_word_str, 'Home & Garden, Home & Garden'))
        nlp_title_list.append((check_word.similarity(home_home_garden_bed_bath_bathroom), check_word_str, 'Home & Garden, Home Garden Bed Bath Bathroom'))
        nlp_title_list.append((check_word.similarity(home_home_garden_domestic_services_cleaning_services), check_word_str, 'Home & Garden, Services Cleaning Services'))
        nlp_title_list.append((check_word.similarity(home_home_garden_laundry), check_word_str, 'Home & Garden, Home Garden Laundry'))
        nlp_title_list.append((check_word.similarity(home_home_garden_yard_patio_lawn_mowers), check_word_str, 'Home & Garden, Home Garden Yard Patio Lawn Mowers'))
        nlp_title_list.append((check_word.similarity(home_home_gardening), check_word_str, 'Home & Garden, Home Gardening'))
        nlp_title_list.append((check_word.similarity(home_home_gym), check_word_str, 'Home & Garden, Home Gym'))
        nlp_title_list.append((check_word.similarity(home_home_hvac), check_word_str, 'Home & Garden, Home HVAC'))
        nlp_title_list.append((check_word.similarity(home_home_improvement), check_word_str, 'Home & Garden, Home Improvement'))
        nlp_title_list.append((check_word.similarity(home_home_improvement_doors), check_word_str, 'Home & Garden, Home Improvement Doors'))
        nlp_title_list.append((check_word.similarity(home_home_improvement_flooring), check_word_str, 'Home & Garden, Home Improvement Flooring'))
        nlp_title_list.append((check_word.similarity(home_home_improvement_plumbing), check_word_str, 'Home & Garden, Home Improvement Plumbing'))
        nlp_title_list.append((check_word.similarity(home_home_improvement_windows), check_word_str, 'Home & Garden, Home Improvement Windows'))
        nlp_title_list.append((check_word.similarity(home_home_kitchen), check_word_str, 'Home & Garden, Home Kitchen'))
        nlp_title_list.append((check_word.similarity(home_home_landscaping), check_word_str, 'Home & Garden, Home Landscaping'))
        nlp_title_list.append((check_word.similarity(home_home_lighting), check_word_str, 'Home & Garden, Home Lighting'))
        nlp_title_list.append((check_word.similarity(home_home_nursery), check_word_str, 'Home & Garden, Home Nursery'))
        nlp_title_list.append((check_word.similarity(home_home_pest_control), check_word_str, 'Home & Garden, Home Pest Control'))
        nlp_title_list.append((check_word.similarity(home_home_playroom), check_word_str, 'Home & Garden, Home Playroom'))
        nlp_title_list.append((check_word.similarity(home_home_plumbing), check_word_str, 'Home & Garden, Home Plumbing'))
        nlp_title_list.append((check_word.similarity(home_home_rugs), check_word_str, 'Home & Garden, Home Rugs'))
        nlp_title_list.append((check_word.similarity(home_home_safety), check_word_str, 'Home & Garden, Home Safety'))
        nlp_title_list.append((check_word.similarity(home_home_saunas), check_word_str, 'Home & Garden, Home Saunas'))
        nlp_title_list.append((check_word.similarity(home_home_security), check_word_str, 'Home & Garden, Home Security'))
        nlp_title_list.append((check_word.similarity(home_home_shelving), check_word_str, 'Home & Garden, Home Shelving'))
        nlp_title_list.append((check_word.similarity(home_home_spas), check_word_str, 'Home & Garden, Home Spas'))
        nlp_title_list.append((check_word.similarity(home_home_storage), check_word_str, 'Home & Garden, Home Storage'))
        nlp_title_list.append((check_word.similarity(home_home_stoves), check_word_str, 'Home & Garden, Home Stoves'))
        nlp_title_list.append((check_word.similarity(home_home_swimming_pools), check_word_str, 'Home & Garden, Home Swimming Pools'))
        nlp_title_list.append((check_word.similarity(home_home_washers), check_word_str, 'Home & Garden, Home Washers'))
        nlp_title_list.append((check_word.similarity(home_home_windows), check_word_str, 'Home & Garden, Home Windows'))
        nlp_title_list.append((check_word.similarity(home_house_finishing), check_word_str, 'Home & Garden, House Finishing'))
        nlp_title_list.append((check_word.similarity(home_house_painting), check_word_str, 'Home & Garden, House Painting'))
        nlp_title_list.append((check_word.similarity(home_interior_decor), check_word_str, 'Home & Garden, Interior Decor'))
        nlp_title_list.append((check_word.similarity(home_lamps), check_word_str, 'Home & Garden, Lamps'))
        nlp_title_list.append((check_word.similarity(home_living_room_furniture), check_word_str, 'Home & Garden, Living Room Furniture'))
        nlp_title_list.append((check_word.similarity(home_major_kitchen_appliances), check_word_str, 'Home & Garden, Major Kitchen Appliances'))
        nlp_title_list.append((check_word.similarity(home_patio), check_word_str, 'Home & Garden, Patio'))
        nlp_title_list.append((check_word.similarity(home_patio_funiture), check_word_str, 'Home & Garden, Patio Funiture'))
        nlp_title_list.append((check_word.similarity(home_pest_control), check_word_str, 'Home & Garden, Pest Control'))
        nlp_title_list.append((check_word.similarity(home_power_tools), check_word_str, 'Home & Garden, Power Tools'))
        nlp_title_list.append((check_word.similarity(home_roofing), check_word_str, 'Home & Garden, Roofing'))
        nlp_title_list.append((check_word.similarity(home_siding), check_word_str, 'Home & Garden, Siding'))
        nlp_title_list.append((check_word.similarity(home_small_kitchen_appliances), check_word_str, 'Home & Garden, Small Kitchen Appliances'))
        nlp_title_list.append((check_word.similarity(home_window_treatments), check_word_str, 'Home & Garden, Window Treatments'))
        nlp_title_list.append((check_word.similarity(home_yard), check_word_str, 'Home & Garden, Yard'))
        nlp_title_list.append((check_word.similarity(internet_affiliate_programs), check_word_str, 'Internet & Telecom, Affiliate Programs'))
        nlp_title_list.append((check_word.similarity(internet_cable_providers), check_word_str, 'Internet & Telecom, Cable Providers'))
        nlp_title_list.append((check_word.similarity(internet_cable_satellite_providers), check_word_str, 'Internet & Telecom, Cable Satellite Providers'))
        nlp_title_list.append((check_word.similarity(internet_communication_equipment), check_word_str, 'Internet & Telecom, Communication Equipment'))
        nlp_title_list.append((check_word.similarity(internet_email), check_word_str, 'Internet & Telecom, Email'))
        nlp_title_list.append((check_word.similarity(internet_instant_messaging), check_word_str, 'Internet & Telecom, Instant Messaging'))
        nlp_title_list.append((check_word.similarity(internet_internet), check_word_str, 'Internet & Telecom, Internet'))
        nlp_title_list.append((check_word.similarity(internet_internet_service_providers), check_word_str, 'Internet & Telecom, Internet Service Providers'))
        nlp_title_list.append((check_word.similarity(internet_internet_services), check_word_str, 'Internet & Telecom, Internet Services'))
        nlp_title_list.append((check_word.similarity(internet_mobile_accessories), check_word_str, 'Internet & Telecom, Mobile Accessories'))
        nlp_title_list.append((check_word.similarity(internet_mobile_add_ons), check_word_str, 'Internet & Telecom, Mobile Add Ons'))
        nlp_title_list.append((check_word.similarity(internet_mobile_apps), check_word_str, 'Internet & Telecom, Mobile Apps'))
        nlp_title_list.append((check_word.similarity(internet_mobile_communications), check_word_str, 'Internet & Telecom, Mobile Communications'))
        nlp_title_list.append((check_word.similarity(internet_mobile_phones), check_word_str, 'Internet & Telecom, Mobile Phones'))
        nlp_title_list.append((check_word.similarity(internet_opera_browser), check_word_str, 'Internet & Telecom, Opera Browser'))
        nlp_title_list.append((check_word.similarity(internet_radio_equipment), check_word_str, 'Internet & Telecom, Radio Equipment'))
        nlp_title_list.append((check_word.similarity(internet_search), check_word_str, 'Internet & Telecom, Search Engines'))
        nlp_title_list.append((check_word.similarity(internet_seo), check_word_str, 'Internet & Telecom, SEO'))
        nlp_title_list.append((check_word.similarity(internet_telecom), check_word_str, 'Internet & Telecom, Telecom'))
        nlp_title_list.append((check_word.similarity(internet_telecom_equipment), check_word_str, 'Internet & Telecom, Telecom Equipment'))
        nlp_title_list.append((check_word.similarity(internet_text_messaging), check_word_str, 'Internet & Telecom, Text Messaging'))
        nlp_title_list.append((check_word.similarity(internet_video_chat), check_word_str, 'Internet & Telecom, Video Chat'))
        nlp_title_list.append((check_word.similarity(internet_voice_chat), check_word_str, 'Internet & Telecom, Voice Chat'))
        nlp_title_list.append((check_word.similarity(internet_web_design), check_word_str, 'Internet & Telecom, Web Design'))
        nlp_title_list.append((check_word.similarity(internet_web_development), check_word_str, 'Internet & Telecom, Web Development'))
        nlp_title_list.append((check_word.similarity(internet_web_services), check_word_str, 'Internet & Telecom, Web Services'))
        nlp_title_list.append((check_word.similarity(internet_website), check_word_str, 'Internet & Telecom, Websites'))
        nlp_title_list.append((check_word.similarity(internet_wireless), check_word_str, 'Internet & Telecom, Wireless'))
        nlp_title_list.append((check_word.similarity(internet_wireless_accessories), check_word_str, 'Internet & Telecom, Wireless Accessories'))
        nlp_title_list.append((check_word.similarity(jobs_career_planning), check_word_str, 'Jobs & Education, Career Planning'))
        nlp_title_list.append((check_word.similarity(jobs_career_resources), check_word_str, 'Jobs & Education, Career Resources'))
        nlp_title_list.append((check_word.similarity(jobs_careers), check_word_str, 'Jobs & Education, Careers'))
        nlp_title_list.append((check_word.similarity(jobs_classroom_resources), check_word_str, 'Jobs & Education, Classroom Resources'))
        nlp_title_list.append((check_word.similarity(jobs_colleges), check_word_str, 'Jobs & Education, Colleges'))
        nlp_title_list.append((check_word.similarity(jobs_continuing_education), check_word_str, 'Jobs & Education, Continuing Education'))
        nlp_title_list.append((check_word.similarity(jobs_distance_learning), check_word_str, 'Jobs & Education, Distance Learning'))
        nlp_title_list.append((check_word.similarity(jobs_employment), check_word_str, 'Jobs & Education, Employment'))
        nlp_title_list.append((check_word.similarity(jobs_homeschooling), check_word_str, 'Jobs & Education, Homeschooling'))
        nlp_title_list.append((check_word.similarity(jobs_job_education), check_word_str, 'Jobs & Education, Job Education'))
        nlp_title_list.append((check_word.similarity(jobs_job_listings), check_word_str, 'Jobs & Education, Job Listings'))
        nlp_title_list.append((check_word.similarity(jobs_jobs), check_word_str, 'Jobs & Education, Jobs'))
        nlp_title_list.append((check_word.similarity(jobs_jobs_planning), check_word_str, 'Jobs & Education, Jobs Planning'))
        nlp_title_list.append((check_word.similarity(jobs_jobs_portfolios), check_word_str, 'Jobs & Education, Jobs Portfolios'))
        nlp_title_list.append((check_word.similarity(jobs_jobs_resources), check_word_str, 'Jobs & Education, Jobs Resources'))
        nlp_title_list.append((check_word.similarity(jobs_jobs_resumes), check_word_str, 'Jobs & Education, Jobs Resumes'))
        nlp_title_list.append((check_word.similarity(jobs_k_12), check_word_str, 'Jobs & Education, K 12'))
        nlp_title_list.append((check_word.similarity(jobs_online_courses), check_word_str, 'Jobs & Education, Online'))
        nlp_title_list.append((check_word.similarity(jobs_primary_schooling_k_12), check_word_str, 'Jobs & Education, Primary Schooling K 12'))
        nlp_title_list.append((check_word.similarity(jobs_remote_education), check_word_str, 'Jobs & Education, Remote Education'))
        nlp_title_list.append((check_word.similarity(jobs_secondary_schooling), check_word_str, 'Jobs & Education, Secondary Schooling'))
        nlp_title_list.append((check_word.similarity(jobs_standardized_admissions_tests), check_word_str, 'Jobs & Education, Standardized Admissions Tests'))
        nlp_title_list.append((check_word.similarity(jobs_teaching_jobs), check_word_str, 'Jobs & Education, Teaching Jobs'))
        nlp_title_list.append((check_word.similarity(jobs_teaching_resources), check_word_str, 'Jobs & Education, Teaching Resources'))
        nlp_title_list.append((check_word.similarity(jobs_training_certification), check_word_str, 'Jobs & Education, Training Certification'))
        nlp_title_list.append((check_word.similarity(jobs_universities), check_word_str, 'Jobs & Education, Universities'))
        nlp_title_list.append((check_word.similarity(jobs_vocational_education), check_word_str, 'Jobs & Education, Vocational Education'))
        nlp_title_list.append((check_word.similarity(law_bankruptcy), check_word_str, 'Law & Government, Bankruptcy'))
        nlp_title_list.append((check_word.similarity(law_crime), check_word_str, 'Law & Government, Crime'))
        nlp_title_list.append((check_word.similarity(law_dui), check_word_str, 'Law & Government, DUI'))
        nlp_title_list.append((check_word.similarity(law_emergency_services), check_word_str, 'Law & Government, Emergency Services'))
        nlp_title_list.append((check_word.similarity(law_evidence), check_word_str, 'Law & Government, Evidence'))
        nlp_title_list.append((check_word.similarity(law_government), check_word_str, 'Law & Government, Government'))
        nlp_title_list.append((check_word.similarity(law_government_laws), check_word_str, 'Law & Government, Government Laws'))
        nlp_title_list.append((check_word.similarity(law_government_security), check_word_str, 'Law & Government, Government Security'))
        nlp_title_list.append((check_word.similarity(law_immigration_law), check_word_str, 'Law & Government, Immigration Law'))
        nlp_title_list.append((check_word.similarity(law_incarceration), check_word_str, 'Law & Government, Incarceration'))
        nlp_title_list.append((check_word.similarity(law_judiciary), check_word_str, 'Law & Government, Judiciary'))
        nlp_title_list.append((check_word.similarity(law_justice), check_word_str, 'Law & Government, Justice'))
        nlp_title_list.append((check_word.similarity(law_law), check_word_str, 'Law & Government, Law'))
        nlp_title_list.append((check_word.similarity(law_law_courts), check_word_str, 'Law & Government, Law Courts'))
        nlp_title_list.append((check_word.similarity(law_law_enforcement), check_word_str, 'Law & Government, Law Enforcement'))
        nlp_title_list.append((check_word.similarity(law_law_military), check_word_str, 'Law & Government, Law Military'))
        nlp_title_list.append((check_word.similarity(law_lawyers), check_word_str, 'Law & Government, Lawyers'))
        nlp_title_list.append((check_word.similarity(law_legal), check_word_str, 'Law & Government, Legal'))
        nlp_title_list.append((check_word.similarity(law_legal_education), check_word_str, 'Law & Government, Legal Education'))
        nlp_title_list.append((check_word.similarity(law_legal_services), check_word_str, 'Law & Government, Legal Services'))
        nlp_title_list.append((check_word.similarity(law_public_safety), check_word_str, 'Law & Government, Public Safety'))
        nlp_title_list.append((check_word.similarity(law_public_safety_services), check_word_str, 'Law & Government, Public Safety Services'))
        nlp_title_list.append((check_word.similarity(law_security_products), check_word_str, 'Law & Government, Security Products'))
        nlp_title_list.append((check_word.similarity(law_security_servicess), check_word_str, 'Law & Government, Security Servicess'))
        nlp_title_list.append((check_word.similarity(law_social_services), check_word_str, 'Law & Government, Social Services'))
        nlp_title_list.append((check_word.similarity(law_visa_law), check_word_str, 'Law & Government, Visa Law'))
        nlp_title_list.append((check_word.similarity(news_business_news), check_word_str, 'News, Business News'))
        nlp_title_list.append((check_word.similarity(news_company_news), check_word_str, 'News, Company News'))
        nlp_title_list.append((check_word.similarity(news_disasters), check_word_str, 'News, Disasters'))
        nlp_title_list.append((check_word.similarity(news_economics_news), check_word_str, 'News, Economics News'))
        nlp_title_list.append((check_word.similarity(news_financial_news), check_word_str, 'News, Financial News'))
        nlp_title_list.append((check_word.similarity(news_gossip), check_word_str, 'News, Gossip'))
        nlp_title_list.append((check_word.similarity(news_health_news), check_word_str, 'News, Health News'))
        nlp_title_list.append((check_word.similarity(news_industry_news), check_word_str, 'News, Industry News'))
        nlp_title_list.append((check_word.similarity(news_investigation_news), check_word_str, 'News, Investigation News'))
        nlp_title_list.append((check_word.similarity(news_magazines), check_word_str, 'News, Magazines'))
        nlp_title_list.append((check_word.similarity(news_markets_news), check_word_str, 'News, Markets News'))
        nlp_title_list.append((check_word.similarity(news_news), check_word_str, 'News, News'))
        nlp_title_list.append((check_word.similarity(news_news_politics), check_word_str, 'News, News Politics'))
        nlp_title_list.append((check_word.similarity(news_news_politics_capitalism), check_word_str, 'News, Capitalism'))
        nlp_title_list.append((check_word.similarity(news_news_politics_communism), check_word_str, 'News & Politics, Communism'))
        nlp_title_list.append((check_word.similarity(news_news_politics_democrats), check_word_str, 'News & Politics, Democrat Party'))
        nlp_title_list.append((check_word.similarity(news_news_politics_fascism), check_word_str, 'News & Politics, Fascism'))
        nlp_title_list.append((check_word.similarity(news_news_politics_feminism), check_word_str, 'News, Feminism'))
        nlp_title_list.append((check_word.similarity(news_news_politics_green_party), check_word_str, 'News & Politics, Green Party'))
        nlp_title_list.append((check_word.similarity(news_news_politics_libertarian), check_word_str, 'News & Politics, Libertarian'))
        nlp_title_list.append((check_word.similarity(news_news_politics_libertarianism), check_word_str, 'News, Libertarianism'))
        nlp_title_list.append((check_word.similarity(news_news_politics_republicans), check_word_str, 'News & Politics, Republican Party'))
        nlp_title_list.append((check_word.similarity(news_news_politics_socialism), check_word_str, 'News, Socialism'))
        nlp_title_list.append((check_word.similarity(news_news_sports_news), check_word_str, 'News, News Sports News'))
        nlp_title_list.append((check_word.similarity(news_news_weather), check_word_str, 'News, News Weather'))
        nlp_title_list.append((check_word.similarity(news_newspapers), check_word_str, 'News, Newspapers'))
        nlp_title_list.append((check_word.similarity(news_scandals), check_word_str, 'News, Scandals'))
        nlp_title_list.append((check_word.similarity(news_tabloid), check_word_str, 'News, Tabloid'))
        nlp_title_list.append((check_word.similarity(online_animated_gifs), check_word_str, 'Online Communities, Animated Gifs'))
        nlp_title_list.append((check_word.similarity(online_blogging), check_word_str, 'Online Communities, Blogging'))
        nlp_title_list.append((check_word.similarity(online_communities), check_word_str, 'Online Communities, Communities'))
        nlp_title_list.append((check_word.similarity(online_communities_social_networks), check_word_str, 'Online Communities, Communities Social Networks'))
        nlp_title_list.append((check_word.similarity(online_communities_virtual_worlds), check_word_str, 'Online Communities, Communities Virtual Worlds'))
        nlp_title_list.append((check_word.similarity(online_design_skins), check_word_str, 'Online Communities, Design Skins'))
        nlp_title_list.append((check_word.similarity(online_design_themes), check_word_str, 'Online Communities, Design Themes'))
        nlp_title_list.append((check_word.similarity(online_design_wallpapers), check_word_str, 'Online Communities, Design Wallpapers'))
        nlp_title_list.append((check_word.similarity(online_file_hosting), check_word_str, 'Online Communities, File Hosting'))
        nlp_title_list.append((check_word.similarity(online_file_sharing), check_word_str, 'Online Communities, File Sharing'))
        nlp_title_list.append((check_word.similarity(online_free_online), check_word_str, 'Online Communities, Free Online'))
        nlp_title_list.append((check_word.similarity(online_online_dating), check_word_str, 'Online Communities, Online Dating'))
        nlp_title_list.append((check_word.similarity(online_online_matrimonial), check_word_str, 'Online Communities, Online Matrimonial'))
        nlp_title_list.append((check_word.similarity(online_online_personals), check_word_str, 'Online Communities, Online Personals'))
        nlp_title_list.append((check_word.similarity(online_photo_rating), check_word_str, 'Online Communities, Photo Rating'))
        nlp_title_list.append((check_word.similarity(online_photo_sharing), check_word_str, 'Online Communities, Photo Sharing'))
        nlp_title_list.append((check_word.similarity(online_social_network_apps), check_word_str, 'Online Communities, Social Network Apps'))
        nlp_title_list.append((check_word.similarity(online_social_networks), check_word_str, 'Online Communities, Social Networks'))
        nlp_title_list.append((check_word.similarity(online_video_sharing), check_word_str, 'Online Communities, Video Sharing'))
        nlp_title_list.append((check_word.similarity(online_virtual_worlds), check_word_str, 'Online Communities, Virtual Worlds'))
        nlp_title_list.append((check_word.similarity(real_estate_commercial_properties), check_word_str, 'Real Estate, Commercial Properties'))
        nlp_title_list.append((check_word.similarity(real_estate_foreclosed_properties), check_word_str, 'Real Estate, Foreclosed Properties'))
        nlp_title_list.append((check_word.similarity(real_estate_listings_rentals), check_word_str, 'Real Estate, Listings Rentals'))
        nlp_title_list.append((check_word.similarity(real_estate_listings_residential), check_word_str, 'Real Estate, Listings Residential'))
        nlp_title_list.append((check_word.similarity(real_estate_real_estate), check_word_str, 'Real Estate, Real Estate'))
        nlp_title_list.append((check_word.similarity(real_estate_real_estate_land), check_word_str, 'Real Estate, Real Estate Land'))
        nlp_title_list.append((check_word.similarity(real_estate_real_estate_listings), check_word_str, 'Real Estate, Real Estate Listings'))
        nlp_title_list.append((check_word.similarity(real_estate_real_estate_lots), check_word_str, 'Real Estate, Real Estate Lots'))
        nlp_title_list.append((check_word.similarity(real_estate_real_estate_services), check_word_str, 'Real Estate, Real Estate Services'))
        nlp_title_list.append((check_word.similarity(real_estate_residential_sales), check_word_str, 'Real Estate, Residential Sales'))
        nlp_title_list.append((check_word.similarity(real_estate_timeshares), check_word_str, 'Real Estate, Timeshares'))
        nlp_title_list.append((check_word.similarity(real_estate_vacation_properties), check_word_str, 'Real Estate, Vacation Properties'))
        nlp_title_list.append((check_word.similarity(reference_arabic_resources), check_word_str, 'Reference, Arabic Language'))
        nlp_title_list.append((check_word.similarity(reference_autobiographies), check_word_str, 'Reference, Autobiographies'))
        nlp_title_list.append((check_word.similarity(reference_biographies), check_word_str, 'Reference, Biographies'))
        nlp_title_list.append((check_word.similarity(reference_business_listings), check_word_str, 'Reference, Business Listings'))
        nlp_title_list.append((check_word.similarity(reference_calculators), check_word_str, 'Reference, Calculators'))
        nlp_title_list.append((check_word.similarity(reference_calendars), check_word_str, 'Reference, Calendars'))
        nlp_title_list.append((check_word.similarity(reference_chinese_resources), check_word_str, 'Reference, Chinese Language'))
        nlp_title_list.append((check_word.similarity(reference_dictionaries), check_word_str, 'Reference, Dictionaries'))
        nlp_title_list.append((check_word.similarity(reference_directories), check_word_str, 'Reference, Directories'))
        nlp_title_list.append((check_word.similarity(reference_encyclopedias), check_word_str, 'Reference, Encyclopedias'))
        nlp_title_list.append((check_word.similarity(reference_english_resources), check_word_str, 'Reference, English Language'))
        nlp_title_list.append((check_word.similarity(reference_folklore), check_word_str, 'Reference, Folklore'))
        nlp_title_list.append((check_word.similarity(reference_foreign_language_resources), check_word_str, 'Reference, Foreign Language Resources'))
        nlp_title_list.append((check_word.similarity(reference_french_resources), check_word_str, 'Reference, French Language'))
        nlp_title_list.append((check_word.similarity(reference_geographic_reference), check_word_str, 'Reference, Geographic Reference'))
        nlp_title_list.append((check_word.similarity(reference_german_resources), check_word_str, 'Reference, German Language'))
        nlp_title_list.append((check_word.similarity(reference_hindi_resources), check_word_str, 'Reference, Hindi Language'))
        nlp_title_list.append((check_word.similarity(reference_language_resources), check_word_str, 'Reference, Language Resources'))
        nlp_title_list.append((check_word.similarity(reference_languages), check_word_str, 'Reference, Languages'))
        nlp_title_list.append((check_word.similarity(reference_libraries), check_word_str, 'Reference, Libraries'))
        nlp_title_list.append((check_word.similarity(reference_maps), check_word_str, 'Reference, Maps'))
        nlp_title_list.append((check_word.similarity(reference_museums), check_word_str, 'Reference, Museums'))
        nlp_title_list.append((check_word.similarity(reference_myths), check_word_str, 'Reference, Myths'))
        nlp_title_list.append((check_word.similarity(reference_personal_listings), check_word_str, 'Reference, Personal Listings'))
        nlp_title_list.append((check_word.similarity(reference_public_records), check_word_str, 'Reference, Public Records'))
        nlp_title_list.append((check_word.similarity(reference_quotations), check_word_str, 'Reference, Quotations'))
        nlp_title_list.append((check_word.similarity(reference_reference), check_word_str, 'Reference, Reference'))
        nlp_title_list.append((check_word.similarity(reference_reference_forms), check_word_str, 'Reference, Reference Forms'))
        nlp_title_list.append((check_word.similarity(reference_reference_general_reference), check_word_str, 'Reference, Reference General Reference'))
        nlp_title_list.append((check_word.similarity(reference_reference_guides), check_word_str, 'Reference, Reference Guides'))
        nlp_title_list.append((check_word.similarity(reference_reference_history), check_word_str, 'Reference, Reference History'))
        nlp_title_list.append((check_word.similarity(reference_reference_humanities), check_word_str, 'Reference, Reference Humanities'))
        nlp_title_list.append((check_word.similarity(reference_reference_philosophy), check_word_str, 'Reference, Reference Philosophy'))
        nlp_title_list.append((check_word.similarity(reference_reference_time), check_word_str, 'Reference, Reference Time'))
        nlp_title_list.append((check_word.similarity(reference_reference_tools), check_word_str, 'Reference, Reference Tools'))
        nlp_title_list.append((check_word.similarity(reference_resource), check_word_str, 'Reference, Resources'))
        nlp_title_list.append((check_word.similarity(reference_russian_resources), check_word_str, 'Reference, Russian Language'))
        nlp_title_list.append((check_word.similarity(reference_spanish_resources), check_word_str, 'Reference, Spanish Language'))
        nlp_title_list.append((check_word.similarity(reference_templates), check_word_str, 'Reference, Templates'))
        nlp_title_list.append((check_word.similarity(science_astronomy), check_word_str, 'Science, Astronomy'))
        nlp_title_list.append((check_word.similarity(science_atmospheric_science), check_word_str, 'Science, Atmospheric Science'))
        nlp_title_list.append((check_word.similarity(science_biology), check_word_str, 'Science, Biology'))
        nlp_title_list.append((check_word.similarity(science_chemistry), check_word_str, 'Science, Chemistry'))
        nlp_title_list.append((check_word.similarity(science_climate_change), check_word_str, 'Science, Climate Change'))
        nlp_title_list.append((check_word.similarity(science_computer_science), check_word_str, 'Science, Computer Science'))
        nlp_title_list.append((check_word.similarity(science_cosmos), check_word_str, 'Science, Cosmos'))
        nlp_title_list.append((check_word.similarity(science_dynamics), check_word_str, 'Science, Dynamics'))
        nlp_title_list.append((check_word.similarity(science_earth_science), check_word_str, 'Science, Earth Science'))
        nlp_title_list.append((check_word.similarity(science_ecology), check_word_str, 'Science, Ecology'))
        nlp_title_list.append((check_word.similarity(science_engineering), check_word_str, 'Science, Engineering'))
        nlp_title_list.append((check_word.similarity(science_geology), check_word_str, 'Science, Geology'))
        nlp_title_list.append((check_word.similarity(science_global_warming), check_word_str, 'Science, Global Warming'))
        nlp_title_list.append((check_word.similarity(science_laboratory), check_word_str, 'Science, Laboratories'))
        nlp_title_list.append((check_word.similarity(science_mathematics), check_word_str, 'Science, Mathematics'))
        nlp_title_list.append((check_word.similarity(science_nasa), check_word_str, 'Science, NASA'))
        nlp_title_list.append((check_word.similarity(science_nature), check_word_str, 'Science, Nature'))
        nlp_title_list.append((check_word.similarity(science_neuroscience), check_word_str, 'Science, Neuroscience'))
        nlp_title_list.append((check_word.similarity(science_physics), check_word_str, 'Science, Physics'))
        nlp_title_list.append((check_word.similarity(science_planets), check_word_str, 'Science, Planets'))
        nlp_title_list.append((check_word.similarity(science_robotics), check_word_str, 'Science, Robotics'))
        nlp_title_list.append((check_word.similarity(science_science), check_word_str, 'Science, Science'))
        nlp_title_list.append((check_word.similarity(science_science_earth_sciences), check_word_str, 'Science, Science Earth Sciences'))
        nlp_title_list.append((check_word.similarity(science_science_environment), check_word_str, 'Science, Science Environment'))
        nlp_title_list.append((check_word.similarity(science_scientific_institutions), check_word_str, 'Science, Scientific Institutions'))
        nlp_title_list.append((check_word.similarity(science_statistics), check_word_str, 'Science, Statistics'))
        nlp_title_list.append((check_word.similarity(science_technology), check_word_str, 'Science, Technology'))
        nlp_title_list.append((check_word.similarity(sensitive_subjects), check_word_str, 'Sensitive Subjects'))
        nlp_title_list.append((check_word.similarity(shopping), check_word_str, 'Shopping'))
        nlp_title_list.append((check_word.similarity(shopping_building_toys), check_word_str, 'Shopping, Building Toys'))
        nlp_title_list.append((check_word.similarity(shopping_cards_greetings), check_word_str, 'Shopping, Cards Greetings'))
        nlp_title_list.append((check_word.similarity(shopping_classifieds), check_word_str, 'Shopping, Classifieds'))
        nlp_title_list.append((check_word.similarity(shopping_classifieds_buying), check_word_str, 'Shopping, Classifieds Buying'))
        nlp_title_list.append((check_word.similarity(shopping_classifieds_selling), check_word_str, 'Shopping, Classifieds Selling'))
        nlp_title_list.append((check_word.similarity(shopping_consumer_advocacy), check_word_str, 'Shopping, Consumer Advocacy'))
        nlp_title_list.append((check_word.similarity(shopping_consumer_protection), check_word_str, 'Shopping, Consumer Protection'))
        nlp_title_list.append((check_word.similarity(shopping_coupons), check_word_str, 'Shopping, Coupons'))
        nlp_title_list.append((check_word.similarity(shopping_department_stores), check_word_str, 'Shopping, Department Stores'))
        nlp_title_list.append((check_word.similarity(shopping_discounts), check_word_str, 'Shopping, Discounts'))
        nlp_title_list.append((check_word.similarity(shopping_dolls), check_word_str, 'Shopping, Dolls'))
        nlp_title_list.append((check_word.similarity(shopping_dolls_accessories), check_word_str, 'Shopping, Dolls Accessories'))
        nlp_title_list.append((check_word.similarity(shopping_electronic_cigarettes), check_word_str, 'Shopping, Electronic Cigarettes'))
        nlp_title_list.append((check_word.similarity(shopping_entertainment_media), check_word_str, 'Shopping, Entertainment Media'))
        nlp_title_list.append((check_word.similarity(shopping_gifts), check_word_str, 'Shopping, Gifts'))
        nlp_title_list.append((check_word.similarity(shopping_luxury_goods), check_word_str, 'Shopping, Luxury Goods'))
        nlp_title_list.append((check_word.similarity(shopping_malls), check_word_str, 'Shopping, Shopping Malls'))
        nlp_title_list.append((check_word.similarity(shopping_marijuana), check_word_str, 'Shopping, Marijuana'))
        nlp_title_list.append((check_word.similarity(shopping_marijuana_accessories), check_word_str, 'Shopping, Marijuana Accessories'))
        nlp_title_list.append((check_word.similarity(shopping_media_rentals), check_word_str, 'Shopping, Media Rentals'))
        nlp_title_list.append((check_word.similarity(shopping_offers), check_word_str, 'Shopping, Offers'))
        nlp_title_list.append((check_word.similarity(shopping_online_shopping), check_word_str, 'Shopping, Online Shopping'))
        nlp_title_list.append((check_word.similarity(shopping_online_stores), check_word_str, 'Shopping, Online Stores'))
        nlp_title_list.append((check_word.similarity(shopping_outdoor_backpacks), check_word_str, 'Shopping, Backpacks'))
        nlp_title_list.append((check_word.similarity(shopping_outdoor_hiking_boots), check_word_str, 'Shopping, Hiking Boots'))
        nlp_title_list.append((check_word.similarity(shopping_outdoor_tents), check_word_str, 'Shopping, Tents'))
        nlp_title_list.append((check_word.similarity(shopping_photo_services), check_word_str, 'Shopping, Photo Services'))
        nlp_title_list.append((check_word.similarity(shopping_price_comparisons), check_word_str, 'Shopping, Price Comparisons'))
        nlp_title_list.append((check_word.similarity(shopping_ride_on_toys), check_word_str, 'Shopping, Ride On Toys'))
        nlp_title_list.append((check_word.similarity(shopping_ride_on_wagons), check_word_str, 'Shopping, Ride On Wagons'))
        nlp_title_list.append((check_word.similarity(shopping_sales), check_word_str, 'Shopping, Sales & Offers'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_antiques), check_word_str, 'Shopping, Shopping Antiques'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_apparel), check_word_str, 'Shopping, Shopping Apparel'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_athletic_apparel), check_word_str, 'Shopping, Shopping Athletic Apparel'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_auctions), check_word_str, 'Shopping, Shopping Auctions'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_casual_apparel), check_word_str, 'Shopping, Shopping Casual Apparel'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_children_clothing), check_word_str, 'Shopping, Shopping Children Clothing'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_children_shopping), check_word_str, 'Shopping, Shopping Children Shopping'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_clothing_accessories), check_word_str, 'Shopping, Shopping Clothing Accessories'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_collectibles), check_word_str, 'Shopping, Shopping Collectibles'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_consumer_resources), check_word_str, 'Shopping, Shopping Consumer Resources'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_costumes), check_word_str, 'Shopping, Shopping Costumes'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_eyewear), check_word_str, 'Shopping, Shopping Eyewear'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_flowers), check_word_str, 'Shopping, Shopping Flowers'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_footwear), check_word_str, 'Shopping, Shopping Footwear'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_formal_wear), check_word_str, 'Shopping, Shopping Formal Wear'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_gifts), check_word_str, 'Shopping, Shopping Gifts'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_headwear), check_word_str, 'Shopping, Shopping Headwear'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_media), check_word_str, 'Shopping, Shopping Media'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_men), check_word_str, 'Shopping, Shopping Men'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_men_clothing), check_word_str, 'Shopping, Shopping Men Clothing'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_men_shoe), check_word_str, 'Shopping, Men\'s Shoes'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_men_suit), check_word_str, 'Shopping, Men\'s Suits'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_men_tie), check_word_str, 'Shopping, Men\'s Ties'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_special), check_word_str, 'Shopping, Shopping Special'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_swimwear), check_word_str, 'Shopping, Shopping Swimwear'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_toys_die_cast_toy_vehicles), check_word_str, 'Shopping, Shopping Toys Die Cast Toy Vehicles'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_undergarments), check_word_str, 'Shopping, Shopping Undergarments'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_women), check_word_str, 'Shopping, Shopping Women'))
        nlp_title_list.append((check_word.similarity(shopping_shopping_women_clothing), check_word_str, 'Shopping, Shopping Women Clothing'))
        nlp_title_list.append((check_word.similarity(shopping_smokeless_tobacco), check_word_str, 'Shopping, Smokeless Tobacco'))
        nlp_title_list.append((check_word.similarity(shopping_smoking_accessories), check_word_str, 'Shopping, Smoking Accessories'))
        nlp_title_list.append((check_word.similarity(shopping_sports_equipment), check_word_str, 'Shopping, Sports Equipment'))
        nlp_title_list.append((check_word.similarity(shopping_stuffed_toys), check_word_str, 'Shopping, Stuffed Toys'))
        nlp_title_list.append((check_word.similarity(shopping_tobacco), check_word_str, 'Shopping, Tobacco'))
        nlp_title_list.append((check_word.similarity(shopping_tobacco_accessories), check_word_str, 'Shopping, Tobacco Accessories'))
        nlp_title_list.append((check_word.similarity(shopping_tobacco_cigarettes), check_word_str, 'Shopping, Tobacco Cigarettes'))
        nlp_title_list.append((check_word.similarity(shopping_tobacco_cigars), check_word_str, 'Shopping, Tobacco Cigars'))
        nlp_title_list.append((check_word.similarity(shopping_tobacco_pipe), check_word_str, 'Shopping, Tobacco Pipe'))
        nlp_title_list.append((check_word.similarity(shopping_toys), check_word_str, 'Shopping, Toys'))
        nlp_title_list.append((check_word.similarity(shopping_vaping), check_word_str, 'Shopping, Vaping'))
        nlp_title_list.append((check_word.similarity(shopping_video_services), check_word_str, 'Shopping, Video Services'))
        nlp_title_list.append((check_word.similarity(society_advocacy_labor), check_word_str, 'Society & People, Advocacy Labor'))
        nlp_title_list.append((check_word.similarity(society_babies), check_word_str, 'Society & People, Babies'))
        nlp_title_list.append((check_word.similarity(society_beliefs), check_word_str, 'Society & People, Beliefs'))
        nlp_title_list.append((check_word.similarity(society_bisexual), check_word_str, 'Society & People, Bisexual'))
        nlp_title_list.append((check_word.similarity(society_charity), check_word_str, 'Society & People, Charity'))
        nlp_title_list.append((check_word.similarity(society_childhood), check_word_str, 'Society & People, Childhood'))
        nlp_title_list.append((check_word.similarity(society_children), check_word_str, 'Society & People, Children'))
        nlp_title_list.append((check_word.similarity(society_church), check_word_str, 'Society & People, Churches'))
        nlp_title_list.append((check_word.similarity(society_culture), check_word_str, 'Society & People, Culture'))
        nlp_title_list.append((check_word.similarity(society_dating), check_word_str, 'Society & People, Dating'))
        nlp_title_list.append((check_word.similarity(society_debates), check_word_str, 'Society & People, Debates'))
        nlp_title_list.append((check_word.similarity(society_dependents), check_word_str, 'Society & People, Dependents'))
        nlp_title_list.append((check_word.similarity(society_discrimination_advocacy), check_word_str, 'Society & People, Discrimination Advocacy'))
        nlp_title_list.append((check_word.similarity(society_economics), check_word_str, 'Society & People, Economics'))
        nlp_title_list.append((check_word.similarity(society_environmental_advocacy), check_word_str, 'Society & People, Environmental Advocacy'))
        nlp_title_list.append((check_word.similarity(society_family_relationship_aunt), check_word_str, 'Society & Relationships, Aunt'))
        nlp_title_list.append((check_word.similarity(society_family_relationship_boyfriend), check_word_str, 'Society & Relationships, Boyfriend'))
        nlp_title_list.append((check_word.similarity(society_family_relationship_brother), check_word_str, 'Society & Relationships, Brother'))
        nlp_title_list.append((check_word.similarity(society_family_relationship_father), check_word_str, 'Society & People, Fathers'))
        nlp_title_list.append((check_word.similarity(society_family_relationship_girlfriend), check_word_str, 'Society & Relationships, Girlfriend'))
        nlp_title_list.append((check_word.similarity(society_family_relationship_grandchild), check_word_str, 'Society & Relationships, Grandchild'))
        nlp_title_list.append((check_word.similarity(society_family_relationship_grandparent), check_word_str, 'Society & Relationships, Grandparent'))
        nlp_title_list.append((check_word.similarity(society_family_relationship_husband), check_word_str, 'Society & People, Husbands'))
        nlp_title_list.append((check_word.similarity(society_family_relationship_husband), check_word_str, 'Society & People, Husband'))
        nlp_title_list.append((check_word.similarity(society_family_relationship_mother), check_word_str, 'Society & People, Mothers'))
        nlp_title_list.append((check_word.similarity(society_family_relationship_parent), check_word_str, 'Society & People, Parents'))
        nlp_title_list.append((check_word.similarity(society_family_relationship_sister), check_word_str, 'Society & People, Sister'))
        nlp_title_list.append((check_word.similarity(society_family_relationship_uncle), check_word_str, 'Society & People, Uncle'))
        nlp_title_list.append((check_word.similarity(society_family_relationship_wife), check_word_str, 'Society & People, Wife'))
        nlp_title_list.append((check_word.similarity(society_family_relationships), check_word_str, 'Society & People, Family Relationships'))
        nlp_title_list.append((check_word.similarity(society_family_relationships_children), check_word_str, 'Society & People, Family Relationships Children'))
        nlp_title_list.append((check_word.similarity(society_friendship), check_word_str, 'Society & People, Friendship'))
        nlp_title_list.append((check_word.similarity(society_funeral), check_word_str, 'Society & People, Funeral'))
        nlp_title_list.append((check_word.similarity(society_gay), check_word_str, 'Society & People, Gay'))
        nlp_title_list.append((check_word.similarity(society_guns), check_word_str, 'Society & People, Guns'))
        nlp_title_list.append((check_word.similarity(society_human_liberties), check_word_str, 'Society & People, Human Liberties'))
        nlp_title_list.append((check_word.similarity(society_human_rights), check_word_str, 'Society & People, Human Rights'))
        nlp_title_list.append((check_word.similarity(society_hunger), check_word_str, 'Society & People, Hunger'))
        nlp_title_list.append((check_word.similarity(society_identity_advocacy), check_word_str, 'Society & People, Identity Advocacy'))
        nlp_title_list.append((check_word.similarity(society_identity_politics), check_word_str, 'Society & People, Identity Politics'))
        nlp_title_list.append((check_word.similarity(society_kids_teens_children_interests), check_word_str, 'Society & People, Kids Teens Children Interests'))
        nlp_title_list.append((check_word.similarity(society_kids_teens_teen_interests), check_word_str, 'Society & People, Kids Teens Teen Interests'))
        nlp_title_list.append((check_word.similarity(society_labor_issues), check_word_str, 'Society & People, Labor Issues'))
        nlp_title_list.append((check_word.similarity(society_leadership), check_word_str, 'Society & People, Leadership'))
        nlp_title_list.append((check_word.similarity(society_lesbian), check_word_str, 'Society & People, Lesbian'))
        nlp_title_list.append((check_word.similarity(society_lgbtq), check_word_str, 'Society & People, Lgbtq'))
        nlp_title_list.append((check_word.similarity(society_life), check_word_str, 'Society & People, Life'))
        nlp_title_list.append((check_word.similarity(society_living), check_word_str, 'Society & People, Living'))
        nlp_title_list.append((check_word.similarity(society_love), check_word_str, 'Society & People, Love'))
        nlp_title_list.append((check_word.similarity(society_men), check_word_str, 'Society & People, Men'))
        nlp_title_list.append((check_word.similarity(society_mentor), check_word_str, 'Society & People, Mentorship'))
        nlp_title_list.append((check_word.similarity(society_obligation), check_word_str, 'Society & People, Obligation'))
        nlp_title_list.append((check_word.similarity(society_peace), check_word_str, 'Society & People, Peace'))
        nlp_title_list.append((check_word.similarity(society_people), check_word_str, 'Society & People, People'))
        nlp_title_list.append((check_word.similarity(society_philanthropy), check_word_str, 'Society & People, Philanthropy'))
        nlp_title_list.append((check_word.similarity(society_political_science), check_word_str, 'Society & People, Political Science'))
        nlp_title_list.append((check_word.similarity(society_poverty), check_word_str, 'Society & People, Poverty'))
        nlp_title_list.append((check_word.similarity(society_privacy), check_word_str, 'Society & People, Privacy'))
        nlp_title_list.append((check_word.similarity(society_queer), check_word_str, 'Society & People, Queer'))
        nlp_title_list.append((check_word.similarity(society_relations_advocacy), check_word_str, 'Society & People, Relations Advocacy'))
        nlp_title_list.append((check_word.similarity(society_relationship_student), check_word_str, 'Society & People, Students'))
        nlp_title_list.append((check_word.similarity(society_relationship_teacher), check_word_str, 'Society & People, Teachers'))
        nlp_title_list.append((check_word.similarity(society_relationships_marriage), check_word_str, 'Society & People, Relationships Marriage'))
        nlp_title_list.append((check_word.similarity(society_religion), check_word_str, 'Society & People, Religion'))
        nlp_title_list.append((check_word.similarity(society_responsibility), check_word_str, 'Society & People, Responsibility'))
        nlp_title_list.append((check_word.similarity(society_retirement), check_word_str, 'Society & People, Retirement'))
        nlp_title_list.append((check_word.similarity(society_self_defense), check_word_str, 'Society & People, Self Defense'))		
        nlp_title_list.append((check_word.similarity(society_self_improvement), check_word_str, 'Society & People, Self Improvement'))
        nlp_title_list.append((check_word.similarity(society_social_advocacy), check_word_str, 'Society & People, Social Advocacy'))
        nlp_title_list.append((check_word.similarity(society_social_issues), check_word_str, 'Society & People, Social Issues'))
        nlp_title_list.append((check_word.similarity(society_social_justice), check_word_str, 'Society & People, Social Justice'))
        nlp_title_list.append((check_word.similarity(society_social_sciences), check_word_str, 'Society & People, Social Sciences'))
        nlp_title_list.append((check_word.similarity(society_social_sciences_psychology), check_word_str, 'Society & People, Social Sciences Psychology'))
        nlp_title_list.append((check_word.similarity(society_society), check_word_str, 'Society & People, Society'))
        nlp_title_list.append((check_word.similarity(society_straight_sexuality), check_word_str, 'Society & People, Straight Sexuality'))
        nlp_title_list.append((check_word.similarity(society_subcultures_niche_interests), check_word_str, 'Society & People, Subcultures Niche Interests'))
        nlp_title_list.append((check_word.similarity(society_sympathy), check_word_str, 'Society & People, Sympathy'))
        nlp_title_list.append((check_word.similarity(society_teaching), check_word_str, 'Society & People, Teaching'))
        nlp_title_list.append((check_word.similarity(society_teens), check_word_str, 'Society & People, Teens'))
        nlp_title_list.append((check_word.similarity(society_traditions), check_word_str, 'Society & People, Traditions'))
        nlp_title_list.append((check_word.similarity(society_transgender), check_word_str, 'Society & People, Transgender'))
        nlp_title_list.append((check_word.similarity(society_troubled_relationships), check_word_str, 'Society & People, Troubled Relationships'))
        nlp_title_list.append((check_word.similarity(society_war), check_word_str, 'Society & People, War'))
        nlp_title_list.append((check_word.similarity(society_war_crimes), check_word_str, 'Society & People, War Crimes'))
        nlp_title_list.append((check_word.similarity(society_women), check_word_str, 'Society & People, Women'))
        nlp_title_list.append((check_word.similarity(sports_american_football), check_word_str, 'Sports, American Football'))
        nlp_title_list.append((check_word.similarity(sports_american_soccer), check_word_str, 'Sports, American Soccer'))
        nlp_title_list.append((check_word.similarity(sports_animal_sports), check_word_str, 'Sports, Animal Sports'))
        nlp_title_list.append((check_word.similarity(sports_australian_football), check_word_str, 'Sports, Australian Football'))
        nlp_title_list.append((check_word.similarity(sports_auto_racing), check_word_str, 'Sports, Auto Racing'))
        nlp_title_list.append((check_word.similarity(sports_baseball), check_word_str, 'Sports, Baseball'))
        nlp_title_list.append((check_word.similarity(sports_basketball), check_word_str, 'Sports, Basketball'))
        nlp_title_list.append((check_word.similarity(sports_boat_racing), check_word_str, 'Sports, Boat Racing'))
        nlp_title_list.append((check_word.similarity(sports_boxing), check_word_str, 'Sports, Boxing'))
        nlp_title_list.append((check_word.similarity(sports_championships), check_word_str, 'Sports, Championships'))
        nlp_title_list.append((check_word.similarity(sports_coaching), check_word_str, 'Sports, Coaching'))
        nlp_title_list.append((check_word.similarity(sports_coaching_coaching), check_word_str, 'Sports, Coaching Coaching'))
        nlp_title_list.append((check_word.similarity(sports_coaching_training), check_word_str, 'Sports, Coaching Training'))
        nlp_title_list.append((check_word.similarity(sports_college_baseball), check_word_str, 'Sports, College Baseball'))
        nlp_title_list.append((check_word.similarity(sports_college_basketball), check_word_str, 'Sports, College Basketball'))
        nlp_title_list.append((check_word.similarity(sports_college_football), check_word_str, 'Sports, College Football'))
        nlp_title_list.append((check_word.similarity(sports_college_sports), check_word_str, 'Sports, College Sports'))
        nlp_title_list.append((check_word.similarity(sports_combat_sports), check_word_str, 'Sports, Combat Sports'))
        nlp_title_list.append((check_word.similarity(sports_cricket), check_word_str, 'Sports, Cricket'))
        nlp_title_list.append((check_word.similarity(sports_cycling), check_word_str, 'Sports, Cycling'))
        nlp_title_list.append((check_word.similarity(sports_diving), check_word_str, 'Sports, Diving'))
        nlp_title_list.append((check_word.similarity(sports_dog_racing), check_word_str, 'Sports, Dog Racing'))
        nlp_title_list.append((check_word.similarity(sports_drag_racing), check_word_str, 'Sports, Drag Racing'))
        nlp_title_list.append((check_word.similarity(sports_extreme_sports), check_word_str, 'Sports, Extreme Sports'))
        nlp_title_list.append((check_word.similarity(sports_fantasy_sports), check_word_str, 'Sports, Fantasy Sports'))
        nlp_title_list.append((check_word.similarity(sports_football), check_word_str, 'Sports, Football'))
        nlp_title_list.append((check_word.similarity(sports_golf), check_word_str, 'Sports, Golf'))
        nlp_title_list.append((check_word.similarity(sports_gymnastics), check_word_str, 'Sports, Gymnastics'))
        nlp_title_list.append((check_word.similarity(sports_hockey), check_word_str, 'Sports, Hockey'))
        nlp_title_list.append((check_word.similarity(sports_horse_racing), check_word_str, 'Sports, Horse Racing'))
        nlp_title_list.append((check_word.similarity(sports_ice_skating), check_word_str, 'Sports, Ice Skating'))
        nlp_title_list.append((check_word.similarity(sports_international_sports), check_word_str, 'Sports, International Sports'))
        nlp_title_list.append((check_word.similarity(sports_martial_arts), check_word_str, 'Sports, Martial Arts'))
        nlp_title_list.append((check_word.similarity(sports_mlb_american_baseball), check_word_str, 'Sports, MLB American Baseball'))
        nlp_title_list.append((check_word.similarity(sports_mls_american_soccer), check_word_str, 'Sports, MLS American Soccer'))
        nlp_title_list.append((check_word.similarity(sports_motocycle_racing), check_word_str, 'Sports, Motocycle Racing'))
        nlp_title_list.append((check_word.similarity(sports_motor_sports), check_word_str, 'Sports, Motor Sports'))
        nlp_title_list.append((check_word.similarity(sports_nba_american_basketball), check_word_str, 'Sports, NBA American Basketball'))
        nlp_title_list.append((check_word.similarity(sports_nfl_american_football), check_word_str, 'Sports, Nfl American Football'))
        nlp_title_list.append((check_word.similarity(sports_nhl_american_hockey), check_word_str, 'Sports, NHL American Hockey'))
        nlp_title_list.append((check_word.similarity(sports_olympics), check_word_str, 'Sports, Olympics'))
        nlp_title_list.append((check_word.similarity(sports_personal_sports), check_word_str, 'Sports, Personal Sports'))
        nlp_title_list.append((check_word.similarity(sports_pga_american_golf), check_word_str, 'Sports, PGA Pro Golf'))
        nlp_title_list.append((check_word.similarity(sports_pro_baseball), check_word_str, 'Sports, Pro Baseball'))
        nlp_title_list.append((check_word.similarity(sports_pro_basketball), check_word_str, 'Sports, Pro Basketball'))
        nlp_title_list.append((check_word.similarity(sports_pro_cycling), check_word_str, 'Sports, Pro Cycling'))
        nlp_title_list.append((check_word.similarity(sports_pro_golf), check_word_str, 'Sports, Pro Golf'))
        nlp_title_list.append((check_word.similarity(sports_pro_gymnastics), check_word_str, 'Sports, Pro Gymnastics'))
        nlp_title_list.append((check_word.similarity(sports_pro_ice_skating), check_word_str, 'Sports, Pro Ice Skating'))
        nlp_title_list.append((check_word.similarity(sports_pro_racquet_sports), check_word_str, 'Sports, Pro Racquet Sports'))
        nlp_title_list.append((check_word.similarity(sports_pro_skate_sports), check_word_str, 'Sports, Pro Skate Sports'))
        nlp_title_list.append((check_word.similarity(sports_pro_skateboarding), check_word_str, 'Sports, Pro Skateboarding'))
        nlp_title_list.append((check_word.similarity(sports_pro_skating), check_word_str, 'Sports, Pro Skating'))
        nlp_title_list.append((check_word.similarity(sports_pro_tennis), check_word_str, 'Sports, Pro Tennis'))
        nlp_title_list.append((check_word.similarity(sports_racquet_sports), check_word_str, 'Sports, Racquet Sports'))
        nlp_title_list.append((check_word.similarity(sports_racquetball), check_word_str, 'Sports, Racquetball'))
        nlp_title_list.append((check_word.similarity(sports_rugby), check_word_str, 'Sports, Rugby'))
        nlp_title_list.append((check_word.similarity(sports_scuba), check_word_str, 'Sports, Scuba Diving'))
        nlp_title_list.append((check_word.similarity(sports_skate_sports), check_word_str, 'Sports, Skate Sports'))
        nlp_title_list.append((check_word.similarity(sports_skateboarding), check_word_str, 'Sports, Skateboarding'))
        nlp_title_list.append((check_word.similarity(sports_skating), check_word_str, 'Sports, Skating'))
        nlp_title_list.append((check_word.similarity(sports_skiing), check_word_str, 'Sports, Skiing'))
        nlp_title_list.append((check_word.similarity(sports_snowboarding), check_word_str, 'Sports, Snowboarding'))
        nlp_title_list.append((check_word.similarity(sports_soccer), check_word_str, 'Sports, Soccer'))
        nlp_title_list.append((check_word.similarity(sports_sporting_goods), check_word_str, 'Sports, Sporting Goods'))
        nlp_title_list.append((check_word.similarity(sports_sports), check_word_str, 'Sports, Sports'))
        nlp_title_list.append((check_word.similarity(sports_sports_memorabilia), check_word_str, 'Sports, Sports Memorabilia'))
        nlp_title_list.append((check_word.similarity(sports_sports_surfing), check_word_str, 'Sports, Sports Surfing'))
        nlp_title_list.append((check_word.similarity(sports_sports_swimming), check_word_str, 'Sports, Sports Swimming'))
        nlp_title_list.append((check_word.similarity(sports_sports_team), check_word_str, 'Sports, Sports Team'))
        nlp_title_list.append((check_word.similarity(sports_sports_water_sports), check_word_str, 'Sports, Sports Water Sports'))
        nlp_title_list.append((check_word.similarity(sports_street_racing), check_word_str, 'Sports, Street Racing'))
        nlp_title_list.append((check_word.similarity(sports_summer_sports), check_word_str, 'Sports, Summer Sports'))
        nlp_title_list.append((check_word.similarity(sports_team_baseball), check_word_str, 'Sports, Team Baseball'))
        nlp_title_list.append((check_word.similarity(sports_team_basketball), check_word_str, 'Sports, Team Basketball'))
        nlp_title_list.append((check_word.similarity(sports_team_cheerleading), check_word_str, 'Sports, Team Cheerleading'))
        nlp_title_list.append((check_word.similarity(sports_team_cricket), check_word_str, 'Sports, Team Cricket'))
        nlp_title_list.append((check_word.similarity(sports_team_hockey), check_word_str, 'Sports, Team Hockey'))
        nlp_title_list.append((check_word.similarity(sports_team_rugby), check_word_str, 'Sports, Team Rugby'))
        nlp_title_list.append((check_word.similarity(sports_team_soccer), check_word_str, 'Sports, Team Soccer'))
        nlp_title_list.append((check_word.similarity(sports_team_volleyball), check_word_str, 'Sports, Team Volleyball'))
        nlp_title_list.append((check_word.similarity(sports_tennis), check_word_str, 'Sports, Tennis'))
        nlp_title_list.append((check_word.similarity(sports_track_field), check_word_str, 'Sports, Track Field'))
        nlp_title_list.append((check_word.similarity(sports_ufc), check_word_str, 'Sports, UFC Ultimate Fighting Championship'))
        nlp_title_list.append((check_word.similarity(sports_volleyball), check_word_str, 'Sports, Volleyball'))
        nlp_title_list.append((check_word.similarity(sports_winter_sports), check_word_str, 'Sports, Winter Sports'))
        nlp_title_list.append((check_word.similarity(sports_winter_sports_equipment), check_word_str, 'Sports, Winter Sports Equipment'))
        nlp_title_list.append((check_word.similarity(sports_wrestling), check_word_str, 'Sports, Wrestling'))
        nlp_title_list.append((check_word.similarity(travel_accommodations), check_word_str, 'Travel, Accommodations'))
        nlp_title_list.append((check_word.similarity(travel_airport_parking), check_word_str, 'Travel, Airport Parking'))
        nlp_title_list.append((check_word.similarity(travel_airport_transportation), check_word_str, 'Travel, Airport Transportation'))
        nlp_title_list.append((check_word.similarity(travel_car_rental), check_word_str, 'Travel, Car Rental'))
        nlp_title_list.append((check_word.similarity(travel_charters), check_word_str, 'Travel, Charters'))
        nlp_title_list.append((check_word.similarity(travel_cruises), check_word_str, 'Travel, Cruises'))
        nlp_title_list.append((check_word.similarity(travel_destinations_beaches), check_word_str, 'Travel, Destinations Beaches'))
        nlp_title_list.append((check_word.similarity(travel_destinations_islands), check_word_str, 'Travel, Destinations Islands'))
        nlp_title_list.append((check_word.similarity(travel_hotels), check_word_str, 'Travel, Hotels'))
        nlp_title_list.append((check_word.similarity(travel_motels), check_word_str, 'Travel, Motels'))
        nlp_title_list.append((check_word.similarity(travel_mountain_resorts), check_word_str, 'Travel, Mountain Resorts'))
        nlp_title_list.append((check_word.similarity(travel_national_parks), check_word_str, 'Travel, National Parks'))
        nlp_title_list.append((check_word.similarity(travel_nature_preserves), check_word_str, 'Travel, Nature Preserves'))
        nlp_title_list.append((check_word.similarity(travel_parks), check_word_str, 'Travel, Parks'))
        nlp_title_list.append((check_word.similarity(travel_regional_parks), check_word_str, 'Travel, Regional Parks'))
        nlp_title_list.append((check_word.similarity(travel_short_term_stays), check_word_str, 'Travel, Short Term Stays'))
        nlp_title_list.append((check_word.similarity(travel_ski_resorts), check_word_str, 'Travel, Ski Resorts'))
        nlp_title_list.append((check_word.similarity(travel_specialty_travel), check_word_str, 'Travel, Specialty Travel'))
        nlp_title_list.append((check_word.similarity(travel_taxi_services), check_word_str, 'Travel, Taxi Services'))
        nlp_title_list.append((check_word.similarity(travel_theme_parks), check_word_str, 'Travel, Theme Parks'))
        nlp_title_list.append((check_word.similarity(travel_tourism), check_word_str, 'Travel, Tourism'))
        nlp_title_list.append((check_word.similarity(travel_tourist_destinations), check_word_str, 'Travel, Tourist Destinations'))
        nlp_title_list.append((check_word.similarity(travel_tourist_gardens), check_word_str, 'Travel, Tourist Gardens'))
        nlp_title_list.append((check_word.similarity(travel_tours), check_word_str, 'Travel, Tours'))   
        nlp_title_list.append((check_word.similarity(travel_travel), check_word_str, 'Travel, Travel'))
        nlp_title_list.append((check_word.similarity(travel_travel_air_travel), check_word_str, 'Travel, Travel Air Travel'))
        nlp_title_list.append((check_word.similarity(travel_travel_bus), check_word_str, 'Travel, Travel Bus'))
        nlp_title_list.append((check_word.similarity(travel_travel_rail), check_word_str, 'Travel, Travel Rail'))
        nlp_title_list.append((check_word.similarity(travel_travel_train), check_word_str, 'Travel, Travel Train'))
        nlp_title_list.append((check_word.similarity(travel_vacation), check_word_str, 'Travel, Vacationing'))    
        nlp_title_list.append((check_word.similarity(travel_vacation_rentals), check_word_str, 'Travel, Vacation Rentals'))
        nlp_title_list.append((check_word.similarity(travel_zoos), check_word_str, 'Travel, Zoos'))
        nlp_title_list.append((check_word.similarity(vehicle_autos), check_word_str, 'Vehicles, Autos'))
        nlp_title_list.append((check_word.similarity(vehicle_bicycles), check_word_str, 'Vehicles, Bicycles'))
        nlp_title_list.append((check_word.similarity(vehicle_bicycles_accessories), check_word_str, 'Vehicles, Bicycles Accessories'))
        nlp_title_list.append((check_word.similarity(vehicle_bike_parts), check_word_str, 'Vehicles, Bike Parts'))
        nlp_title_list.append((check_word.similarity(vehicle_bike_repair), check_word_str, 'Vehicles, Bike Repair'))
        nlp_title_list.append((check_word.similarity(vehicle_bmx_accessories), check_word_str, 'Vehicles, Bmx Accessories'))
        nlp_title_list.append((check_word.similarity(vehicle_bmx_bikes), check_word_str, 'Vehicles, Bmx Bikes'))
        nlp_title_list.append((check_word.similarity(vehicle_boats), check_word_str, 'Vehicles, Boats'))
        nlp_title_list.append((check_word.similarity(vehicle_buy_car), check_word_str, 'Vehicles, Buy Car'))
        nlp_title_list.append((check_word.similarity(vehicle_buy_used_car), check_word_str, 'Vehicles, Buy Used Car'))
        nlp_title_list.append((check_word.similarity(vehicle_campers), check_word_str, 'Vehicles, Campers'))
        nlp_title_list.append((check_word.similarity(vehicle_car_shows), check_word_str, 'Vehicles, Car Shows'))
        nlp_title_list.append((check_word.similarity(vehicle_cargo_trailers), check_word_str, 'Vehicles, Cargo Trailers'))
        nlp_title_list.append((check_word.similarity(vehicle_cargo_trucks), check_word_str, 'Vehicles, Cargo Trucks'))
        nlp_title_list.append((check_word.similarity(vehicle_classic_cars), check_word_str, 'Vehicles, Classic Cars'))
        nlp_title_list.append((check_word.similarity(vehicle_driving_laws), check_word_str, 'Vehicles, Driving Laws'))
        nlp_title_list.append((check_word.similarity(vehicle_driving_license), check_word_str, 'Vehicles, Driving License'))
        nlp_title_list.append((check_word.similarity(vehicle_electric_cars), check_word_str, 'Vehicles, Electric Cars'))
        nlp_title_list.append((check_word.similarity(vehicle_gas_prices), check_word_str, 'Vehicles, Gas Prices'))
        nlp_title_list.append((check_word.similarity(vehicle_hybrid_cars), check_word_str, 'Vehicles, Hybrid Cars'))
        nlp_title_list.append((check_word.similarity(vehicle_jet_skis), check_word_str, 'Vehicles, Jet Skis'))
        nlp_title_list.append((check_word.similarity(vehicle_motorcycles), check_word_str, 'Vehicles, Motorcycles'))
        nlp_title_list.append((check_word.similarity(vehicle_off_road_vehicles), check_word_str, 'Vehicles, Off Road Vehicles'))
        nlp_title_list.append((check_word.similarity(vehicle_sell_car), check_word_str, 'Vehicles, Sell Car'))
        nlp_title_list.append((check_word.similarity(vehicle_sell_used_car), check_word_str, 'Vehicles, Sell Used Car'))
        nlp_title_list.append((check_word.similarity(vehicle_suvs), check_word_str, 'Vehicles, Suvs'))
        nlp_title_list.append((check_word.similarity(vehicle_trucks), check_word_str, 'Vehicles, Trucks'))
        nlp_title_list.append((check_word.similarity(vehicle_vehicle_accessories), check_word_str, 'Vehicles, Vehicle Accessories'))
        nlp_title_list.append((check_word.similarity(vehicle_vehicle_maintenance), check_word_str, 'Vehicles, Vehicle Maintenance'))
        nlp_title_list.append((check_word.similarity(vehicle_vehicle_parts), check_word_str, 'Vehicles, Vehicle Parts'))
        nlp_title_list.append((check_word.similarity(vehicle_vehicle_registration), check_word_str, 'Vehicles, Vehicle Registration'))
        nlp_title_list.append((check_word.similarity(vehicle_vehicle_repair), check_word_str, 'Vehicles, Vehicle Repair'))
        nlp_title_list.append((check_word.similarity(vehicle_vehicle_services), check_word_str, 'Vehicles, Vehicle Services'))
        nlp_title_list.append((check_word.similarity(vehicle_watercraft), check_word_str, 'Vehicles, Watercraft'))     
        title_list_sorted = (nlargest(20, nlp_title_list))
        for tit_s in title_list_sorted:  
            combined_thoughts.append(tit_s)

    bi_task = asyncio.create_task(async_bi())
    tri_task = asyncio.create_task(async_tri())
    rake_task = asyncio.create_task(async_rake())
    sent_task = asyncio.create_task(sent_func())
    noun_task = asyncio.create_task(noun_func())
    pronoun_task = asyncio.create_task(propnoun_func())
    await asyncio.gather(bi_task, tri_task, rake_task, sent_task, noun_task, pronoun_task)
    tasks_list = []
    for check_word_ch in PROPN_list:
        tasks_list.append(asyncio.create_task(thinker(check_word_ch)))  

    await asyncio.gather(*tasks_list)

    sprk_collection = {"word_count" : word_count, "text_title" : text_title, "bigram_list" : bi_list, "trigram_list" : tri_list, "rake_kw_list" : rake_list}
    article_json = {"nlp_collection" : sprk_collection, "sentences_list" : sentences_list}

    final_thought_sorted = nlargest(100, combined_thoughts)
    combo_list = []

    for combo in final_thought_sorted:
        if combo[0] > .75:
            combo_list.append((combo[0],combo[2]))


    val_2 = collections.Counter([y for (x,y) in combo_list])
    collections_list = []
    over_think_list = [] 
    for x in val_2:
        key = x
        value = val_2[key]
        collections_list.append((value, x))
        over_think_list.append((value, x))

    collections_list = (nlargest(3, collections_list))
    categories_list = []
    for jj in collections_list:
        cat_result_dict = {"rank" : jj[0], "category" : jj[1]}
        categories_list.append(cat_result_dict)

    categories_dict = {"categories_list" : categories_list}

    return categories_dict, article_json, text_title
