PGDMP     	        
            {           actors    15.2    15.2 *    I           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            J           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            K           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            L           1262    16431    actors    DATABASE     �   CREATE DATABASE actors WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = icu LOCALE = 'en_US.UTF-8' ICU_LOCALE = 'en-US';
    DROP DATABASE actors;
                postgres    false            �            1259    16433    actors    TABLE     �   CREATE TABLE public.actors (
    id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(100) NOT NULL,
    birthday date NOT NULL,
    number_oscars bigint NOT NULL
);
    DROP TABLE public.actors;
       public         heap    postgres    false            �            1259    16432    actors_actor_id_seq    SEQUENCE     �   CREATE SEQUENCE public.actors_actor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.actors_actor_id_seq;
       public          postgres    false    215            M           0    0    actors_actor_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.actors_actor_id_seq OWNED BY public.actors.id;
          public          postgres    false    214            �            1259    16483    actors_movies    TABLE     R   CREATE TABLE public.actors_movies (
    actor_id integer,
    movie_id integer
);
 !   DROP TABLE public.actors_movies;
       public         heap    postgres    false            �            1259    16444 	   apartment    TABLE     �   CREATE TABLE public.apartment (
    id integer NOT NULL,
    location character varying(50),
    actor_id integer,
    producer_id integer
);
    DROP TABLE public.apartment;
       public         heap    postgres    false            �            1259    16443    apartment_id_seq    SEQUENCE     �   CREATE SEQUENCE public.apartment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.apartment_id_seq;
       public          postgres    false    217            N           0    0    apartment_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.apartment_id_seq OWNED BY public.apartment.id;
          public          postgres    false    216            �            1259    16477    movies    TABLE     Y   CREATE TABLE public.movies (
    id integer NOT NULL,
    title character varying(50)
);
    DROP TABLE public.movies;
       public         heap    postgres    false            �            1259    16476    movies_id_seq    SEQUENCE     �   CREATE SEQUENCE public.movies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.movies_id_seq;
       public          postgres    false    221            O           0    0    movies_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.movies_id_seq OWNED BY public.movies.id;
          public          postgres    false    220            �            1259    16463 	   producers    TABLE     �   CREATE TABLE public.producers (
    id integer NOT NULL,
    first_name character varying(20) NOT NULL,
    last_name character varying(20) NOT NULL,
    number_oscars integer NOT NULL
);
    DROP TABLE public.producers;
       public         heap    postgres    false            �            1259    16462    producers_id_seq    SEQUENCE     �   CREATE SEQUENCE public.producers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.producers_id_seq;
       public          postgres    false    219            P           0    0    producers_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.producers_id_seq OWNED BY public.producers.id;
          public          postgres    false    218            �            1259    16816    script    TABLE     �   CREATE TABLE public.script (
    movie_id integer NOT NULL,
    title character varying(50),
    author character varying(50),
    story text
);
    DROP TABLE public.script;
       public         heap    postgres    false            �           2604    16436 	   actors id    DEFAULT     l   ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_actor_id_seq'::regclass);
 8   ALTER TABLE public.actors ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            �           2604    16447    apartment id    DEFAULT     l   ALTER TABLE ONLY public.apartment ALTER COLUMN id SET DEFAULT nextval('public.apartment_id_seq'::regclass);
 ;   ALTER TABLE public.apartment ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    216    217            �           2604    16480 	   movies id    DEFAULT     f   ALTER TABLE ONLY public.movies ALTER COLUMN id SET DEFAULT nextval('public.movies_id_seq'::regclass);
 8   ALTER TABLE public.movies ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    220    221            �           2604    16466    producers id    DEFAULT     l   ALTER TABLE ONLY public.producers ALTER COLUMN id SET DEFAULT nextval('public.producers_id_seq'::regclass);
 ;   ALTER TABLE public.producers ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    218    219            >          0    16433    actors 
   TABLE DATA           T   COPY public.actors (id, first_name, last_name, birthday, number_oscars) FROM stdin;
    public          postgres    false    215   �-       E          0    16483    actors_movies 
   TABLE DATA           ;   COPY public.actors_movies (actor_id, movie_id) FROM stdin;
    public          postgres    false    222    .       @          0    16444 	   apartment 
   TABLE DATA           H   COPY public.apartment (id, location, actor_id, producer_id) FROM stdin;
    public          postgres    false    217   &.       D          0    16477    movies 
   TABLE DATA           +   COPY public.movies (id, title) FROM stdin;
    public          postgres    false    221   z.       B          0    16463 	   producers 
   TABLE DATA           M   COPY public.producers (id, first_name, last_name, number_oscars) FROM stdin;
    public          postgres    false    219   �.       F          0    16816    script 
   TABLE DATA           @   COPY public.script (movie_id, title, author, story) FROM stdin;
    public          postgres    false    223   �.       Q           0    0    actors_actor_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.actors_actor_id_seq', 4, true);
          public          postgres    false    214            R           0    0    apartment_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.apartment_id_seq', 7, true);
          public          postgres    false    216            S           0    0    movies_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.movies_id_seq', 1, true);
          public          postgres    false    220            T           0    0    producers_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.producers_id_seq', 2, true);
          public          postgres    false    218            �           2606    16438    actors actors_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.actors DROP CONSTRAINT actors_pkey;
       public            postgres    false    215            �           2606    16449    apartment apartment_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.apartment
    ADD CONSTRAINT apartment_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.apartment DROP CONSTRAINT apartment_pkey;
       public            postgres    false    217            �           2606    16482    movies movies_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.movies DROP CONSTRAINT movies_pkey;
       public            postgres    false    221            �           2606    16468    producers producers_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.producers
    ADD CONSTRAINT producers_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.producers DROP CONSTRAINT producers_pkey;
       public            postgres    false    219            �           2606    16822    script script_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.script
    ADD CONSTRAINT script_pkey PRIMARY KEY (movie_id);
 <   ALTER TABLE ONLY public.script DROP CONSTRAINT script_pkey;
       public            postgres    false    223            �           2606    16486 )   actors_movies actors_movies_actor_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.actors_movies
    ADD CONSTRAINT actors_movies_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES public.actors(id);
 S   ALTER TABLE ONLY public.actors_movies DROP CONSTRAINT actors_movies_actor_id_fkey;
       public          postgres    false    215    3489    222            �           2606    16491 )   actors_movies actors_movies_movie_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.actors_movies
    ADD CONSTRAINT actors_movies_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movies(id);
 S   ALTER TABLE ONLY public.actors_movies DROP CONSTRAINT actors_movies_movie_id_fkey;
       public          postgres    false    221    222    3495            �           2606    16450 !   apartment apartment_actor_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.apartment
    ADD CONSTRAINT apartment_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES public.actors(id);
 K   ALTER TABLE ONLY public.apartment DROP CONSTRAINT apartment_actor_id_fkey;
       public          postgres    false    217    3489    215            �           2606    16823    script df_movie_id    FK CONSTRAINT     s   ALTER TABLE ONLY public.script
    ADD CONSTRAINT df_movie_id FOREIGN KEY (movie_id) REFERENCES public.movies(id);
 <   ALTER TABLE ONLY public.script DROP CONSTRAINT df_movie_id;
       public          postgres    false    221    3495    223            �           2606    16471    apartment fk_producers    FK CONSTRAINT     }   ALTER TABLE ONLY public.apartment
    ADD CONSTRAINT fk_producers FOREIGN KEY (producer_id) REFERENCES public.producers(id);
 @   ALTER TABLE ONLY public.apartment DROP CONSTRAINT fk_producers;
       public          postgres    false    217    219    3493            >   o   x���
�0E���y�6m�Z���n��	�A��m]_�5�b�8�wɰ�@�Fip�<�\J��V{S�ʀFZ\��2N��aT����Z�ZS�����S����� "?�A�      E      x�3�4�2b ����� >      @   D   x�3�tJ-K-ʩT����)�4���2�q�4��8�R�"󋲁<NC.sNǜ���D(���� ]��      D      x�3�(�)PH�L.�������� A�      B   3   x�3�.I��I���.M*���4�2�,M�+���I,J1�9��b���� S��      F   B   x�3�(�)PH�L.����,M�+��SI,J1�9}KsJ2rR�K�2S���KK�b���� ��     