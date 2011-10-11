"""
_Create_

Implementation of Create for Oracle

"""

import threading

from WMCore.Database.DBCreator import DBCreator

class Create(DBCreator):

    def __init__(self, logger = None, dbi = None):
        """
        _init_

        Call the DBCreator constructor and initialize the schema

        """
        myThread = threading.currentThread()
        if logger == None:
            logger = myThread.logger
        if dbi == None:
            dbi = myThread.dbi

        DBCreator.__init__(self, logger, dbi)

        #
        # Tables, functions and procedures
        #
        self.create[len(self.create)] = \
            """CREATE TABLE t0_config (
                 run_id     int          not null,
                 config     varchar(255) not null,
                 primary key(run_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE run_status (
                 id      int           not null,
                 name    varchar(25)   not null,
                 primary key(id),
                 constraint ctr_run_sta_name unique(name)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE processing_style (
                 id    int         not null,
                 name  varchar(25) not null,
                 primary key(id),
                 constraint ctr_pro_sty_name unique(name)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE event_scenario (
                 id      int           not null,
                 name    varchar(25)   not null,
                 primary key(id),
                 constraint ctr_eve_sce_name unique(name)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE cmssw_version (
                 id   int          not null,
                 name varchar(255) not null,
                 primary key(id),
                 constraint ctr_cms_ver_name unique(name)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE stream (
                 id    int            not null,
                 name  varchar(255)   not null,
                 primary key(id),
                 constraint ctr_str_name unique(name)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE trigger_label (
                 id      int           not null,
                 name    varchar(255)  not null,
                 primary key(id),
                 constraint ctr_tri_lab_name unique(name)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE primary_dataset (
                 id      int           not null,
                 name    varchar(255)  not null,
                 primary key(id),
                 constraint ctr_pri_dat_name unique(name)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE run (
                 run_id             int            not null,
                 online_version     int            not null,
                 status             int            not null,
                 last_updated       int            default 0 not null,
                 reco_started       int            default 0 not null,
                 express_started    int            default 0 not null,
                 hltkey             varchar(255)   not null,
                 start_time         int            not null,
                 end_time           int            default 0 not null,
                 close_time         int            default 0 not null,
                 lumicount          int            default 0 not null,
                 reco_timeout       int            default 0 not null,
                 reco_lock_timeout  int            default 0 not null,
                 process            varchar(255),
                 acq_era            varchar(255),
                 primary key(run_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE run_trig_primds_assoc (
                 run_id     int   not null,
                 trig_id    int   not null,
                 primds_id  int   not null,
                 primary key(run_id, trig_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE run_primds_stream_assoc (
                 run_id     int   not null,
                 primds_id  int   not null,
                 stream_id  int   not null,
                 primary key(run_id, primds_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE run_primds_scenario_assoc (
                 run_id       int   not null,
                 primds_id    int   not null,
                 scenario_id  int   not null,
                 primary key(run_id, primds_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE run_stream_style_assoc (
                 run_id    int not null,
                 stream_id int not null,
                 style_id  int not null,
                 primary key(run_id, stream_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE run_stream_cmssw_assoc (
                 run_id           int not null,
                 stream_id        int not null,
                 online_version   int not null,
                 override_version int not null,
                 primary key(run_id, stream_id)
                )"""

        self.create[len(self.create)] = \
            """CREATE TABLE run_stream_sub_assoc (
                 run_id       int   not null,
                 stream_id    int   not null,
                 subscription int   not null,
                 primary key(run_id, stream_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE stream_special_primds_assoc (
                 stream_id    int   not null,
                 primds_id    int   not null,
                 primary key(stream_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE primds_error_primds_assoc (
                 parent_id   int   not null,
                 error_id    int   not null,
                 primary key(parent_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE lumi_section (
                 run_id      int   not null,
                 lumi_id     int   not null,
                 primary key(run_id, lumi_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE lumi_section_closed (
                 run_id      int   not null,
                 stream_id   int   not null,
                 lumi_id     int   not null,
                 filecount   int   not null,
                 insert_time int   not null,
                 close_time  int   default 0 not null,
                 primary key(run_id, stream_id, lumi_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE lumi_section_split_active (
                 run_id      int   not null,
                 stream_id   int   not null,
                 lumi_id     int   not null,
                 primary key(run_id, stream_id, lumi_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE streamer (
                 id              int   not null,
                 run_id          int   not null,
                 stream_id       int   not null,
                 lumi_id         int   not null,
                 insert_time     int   not null,
                 used            int   default 0 not null,
                 deleted         int   default 0 not null,
                 primary key(id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE repack_config (
                 run_id         int not null,
                 stream_id      int not null,
                 proc_version   varchar(255) not null,
                 primary key (run_id, stream_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE express_config (
                 run_id                  int          not null,
                 stream_id               int          not null,
                 splitInProcessing       int          not null,
                 proc_version            varchar(255) not null,
                 write_tiers             varchar(255) not null,
                 global_tag              varchar(255),
                 processing_config_url   varchar(255),
                 alcamerge_config_url    varchar(255),
                 primary key (run_id, stream_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE reco_config (
                  run_id            int not null,
                  primds_id         int not null,
                  do_reco           int not null,
                  cmssw_version_id  int not null,
                  reco_split        int not null,
                  write_reco        int not null,
                  write_dqm         int not null,
                  write_aod         int not null,
                  proc_version      varchar(255) not null,
                  global_tag        varchar(255),
                  config_url        varchar(255),
                  pset_hash         varchar(700),
                  branch_hash       varchar(700),
                  primary key (run_id, primds_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE alca_config (
                  run_id            int not null,
                  primds_id         int not null,
                  do_alca           int not null,
                  cmssw_version_id  int not null,
                  proc_version      varchar(255) not null,
                  write_skims       varchar(1000),
                  config_url        varchar(255),
                  pset_hash         varchar(700),
                  branch_hash       varchar(700),
                  primary key (run_id, primds_id)
               )"""

        self.create[len(self.create)] = \
            """CREATE TABLE promptskim_config (
                  run_id            int not null,
                  primds_id         int not null,
                  data_tier_id      int not null,
                  node_id           int not null,
                  cmssw_version_id  int not null,
                  two_file_read     int not null,
                  proc_version      varchar(255) not null,
                  skim_name         varchar(255) not null,
                  global_tag        varchar(255),
                  config_url        varchar(255),
                  primary key (run_id, primds_id, data_tier_id, skim_name)
               )"""

        self.create[len(self.create)] = \
            """CREATE FUNCTION checkForZeroState (value IN int)
               RETURN int DETERMINISTIC IS
               BEGIN
                 IF value = 0 THEN
                   RETURN 0;
                 ELSE
                   RETURN NULL;
                 END IF;
               END checkForZeroState;
               """

        self.create[len(self.create)] = \
            """CREATE FUNCTION checkForZeroOneState (value IN int)
               RETURN int DETERMINISTIC IS
               BEGIN
                 IF value = 0 THEN
                   RETURN 0;
                 ELSIF value = 1 THEN
                   RETURN 1;
                 ELSE
                   RETURN NULL;
                 END IF;
               END checkForZeroOneState;
               """

        #
        # Indexes
        #
        self.indexes[len(self.indexes)] = \
            """CREATE INDEX idx_run_1 ON run (status)"""

        self.indexes[len(self.indexes)] = \
            """CREATE INDEX idx_run_trig_primds_1 ON run_trig_primds_assoc (run_id, primds_id)"""

        self.indexes[len(self.indexes)] = \
            """CREATE INDEX idx_run_primds_stream_1 ON run_primds_stream_assoc (run_id, stream_id)"""

        self.indexes[len(self.indexes)] = \
            """CREATE INDEX idx_lumi_section_closed_1 ON lumi_section_closed (checkForZeroState(close_time))"""

        self.indexes[len(self.indexes)] = \
            """CREATE INDEX idx_streamer_1 ON streamer (run_id, stream_id, lumi_id)"""

        self.indexes[len(self.indexes)] = \
            """CREATE INDEX idx_streamer_2 ON streamer (checkForZeroState(used))"""

        self.indexes[len(self.indexes)] = \
            """CREATE INDEX idx_streamer_3 ON streamer (checkForZeroOneState(deleted))"""

        #
        # Constraints
        #
        self.constraints[len(self.constraints)] = \
            """ALTER TABLE t0_config
                 ADD CONSTRAINT t0_conf_run_id_fk
                 FOREIGN KEY (run_id)
                 REFERENCES run(run_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run
                 ADD CONSTRAINT run_onl_ver_fk
                 FOREIGN KEY (online_version)
                 REFERENCES cmssw_version(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run
                 ADD CONSTRAINT run_sta_fk
                 FOREIGN KEY (status)
                 REFERENCES run_status(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_trig_primds_assoc
                 ADD CONSTRAINT run_tri_pri_run_id_fk
                 FOREIGN KEY (run_id)
                 REFERENCES run(run_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_trig_primds_assoc
                 ADD CONSTRAINT run_tri_pri_tri_id_fk
                 FOREIGN KEY (trig_id)
                 REFERENCES trigger_label(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_trig_primds_assoc
                 ADD CONSTRAINT run_tri_pri_pri_id_fk
                 FOREIGN KEY (primds_id)
                 REFERENCES primary_dataset(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_primds_stream_assoc
                 ADD CONSTRAINT run_pri_tri_run_id_fk
                 FOREIGN KEY (run_id)
                 REFERENCES run(run_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_primds_stream_assoc
                 ADD CONSTRAINT run_pri_tri_pri_id_fk
                 FOREIGN KEY (primds_id)
                 REFERENCES primary_dataset(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_primds_stream_assoc
                 ADD CONSTRAINT run_pri_tri_str_id_fk
                 FOREIGN KEY (stream_id)
                 REFERENCES stream(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_primds_scenario_assoc
                 ADD CONSTRAINT run_pri_sce_run_id_fk
                 FOREIGN KEY (run_id)
                 REFERENCES run(run_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_primds_scenario_assoc
                 ADD CONSTRAINT run_pri_sce_pri_id_fk
                 FOREIGN KEY (primds_id)
                 REFERENCES primary_dataset(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_primds_scenario_assoc
                 ADD CONSTRAINT run_pri_sce_sce_id_fk
                 FOREIGN KEY (scenario_id)
                 REFERENCES event_scenario(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_stream_style_assoc
                 ADD CONSTRAINT run_str_sty_run_id_fk
                 FOREIGN KEY (run_id)
                 REFERENCES run(run_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_stream_style_assoc
                 ADD CONSTRAINT run_str_sty_str_id_fk
                 FOREIGN KEY (stream_id)
                 REFERENCES stream(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_stream_style_assoc
                 ADD CONSTRAINT run_str_sty_sty_id_fk
                 FOREIGN KEY (style_id)
                 REFERENCES processing_style(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_stream_cmssw_assoc
                 ADD CONSTRAINT run_str_cms_run_id_fk
                 FOREIGN KEY (run_id)
                 REFERENCES run(run_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_stream_cmssw_assoc
                 ADD CONSTRAINT run_str_cms_str_id_fk
                 FOREIGN KEY (stream_id)
                 REFERENCES stream(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_stream_cmssw_assoc
                 ADD CONSTRAINT run_str_cms_onl_ver_fk
                 FOREIGN KEY (online_version)
                 REFERENCES cmssw_version(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_stream_cmssw_assoc
                 ADD CONSTRAINT run_str_cms_ove_ver_fk
                 FOREIGN KEY (override_version)
                 REFERENCES cmssw_version(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_stream_sub_assoc
                 ADD CONSTRAINT run_str_sub_run_id_fk
                 FOREIGN KEY (run_id)
                 REFERENCES run(run_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_stream_sub_assoc
                 ADD CONSTRAINT run_str_sub_str_id_fk
                 FOREIGN KEY (stream_id)
                 REFERENCES stream(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE run_stream_sub_assoc
                 ADD CONSTRAINT run_str_sub_sub_id_fk
                 FOREIGN KEY (subscription)
                 REFERENCES wmbs_subscription(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE stream_special_primds_assoc
                 ADD CONSTRAINT str_spe_pri_str_id_fk
                 FOREIGN KEY (stream_id)
                 REFERENCES stream(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE stream_special_primds_assoc
                 ADD CONSTRAINT str_spe_pri_pri_id_fk
                 FOREIGN KEY (primds_id)
                 REFERENCES primary_dataset(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE primds_error_primds_assoc
                 ADD CONSTRAINT pri_err_pri_par_id_fk
                 FOREIGN KEY (parent_id)
                 REFERENCES primary_dataset(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE primds_error_primds_assoc
                 ADD CONSTRAINT pri_err_pri_err_id_fk
                 FOREIGN KEY (error_id)
                 REFERENCES primary_dataset(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE lumi_section
                 ADD CONSTRAINT lum_sec_run_id_fk
                 FOREIGN KEY (run_id)
                 REFERENCES run(run_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE lumi_section_closed
                 ADD CONSTRAINT lum_sec_clo_rl_id_fk
                 FOREIGN KEY (run_id, lumi_id)
                 REFERENCES lumi_section(run_id, lumi_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE lumi_section_closed
                 ADD CONSTRAINT lum_sec_clo_stre_id_fk
                 FOREIGN KEY (stream_id)
                 REFERENCES stream(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE lumi_section_split_active
                 ADD CONSTRAINT lum_sec_spli_act_rl_id_fk
                 FOREIGN KEY (run_id, lumi_id)
                 REFERENCES lumi_section(run_id, lumi_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE lumi_section_split_active
                 ADD CONSTRAINT lum_sec_spli_act_stre_id_fk
                 FOREIGN KEY (stream_id)
                 REFERENCES stream(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE streamer
                 ADD CONSTRAINT str_run_id_fk
                 FOREIGN KEY (run_id)
                 REFERENCES run(run_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE streamer
                 ADD CONSTRAINT str_rl_id_fk
                 FOREIGN KEY (run_id, lumi_id)
                 REFERENCES lumi_section(run_id, lumi_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE streamer
                 ADD CONSTRAINT str_str_id_fk
                 FOREIGN KEY (stream_id)
                 REFERENCES stream(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE repack_config
                 ADD CONSTRAINT rep_con_run_id_fk
                 FOREIGN KEY (run_id)
                 REFERENCES run(run_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE repack_config
                 ADD CONSTRAINT rep_con_str_id_fk
                 FOREIGN KEY (stream_id)
                 REFERENCES stream(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE express_config
                 ADD CONSTRAINT exp_con_run_id_fk
                 FOREIGN KEY (run_id)
                 REFERENCES run(run_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE express_config
                 ADD CONSTRAINT exp_con_str_id_fk
                 FOREIGN KEY (stream_id)
                 REFERENCES stream(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE reco_config
                 ADD CONSTRAINT rec_con_run_id_fk
                 FOREIGN KEY (run_id)
                 REFERENCES run(run_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE reco_config
                 ADD CONSTRAINT rec_con_primds_id_fk
                 FOREIGN KEY (primds_id)
                 REFERENCES primary_dataset(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE reco_config
                 ADD CONSTRAINT rec_con_cms_id_fk
                 FOREIGN KEY (cmssw_version_id)
                 REFERENCES cmssw_version(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE alca_config
                 ADD CONSTRAINT alc_con_run_id_fk
                 FOREIGN KEY (run_id)
                 REFERENCES run(run_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE alca_config
                 ADD CONSTRAINT alc_con_primds_id_fk
                 FOREIGN KEY (primds_id)
                 REFERENCES primary_dataset(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE alca_config
                 ADD CONSTRAINT alc_con_cms_id_fk
                 FOREIGN KEY (cmssw_version_id)
                 REFERENCES cmssw_version(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE promptskim_config
                 ADD CONSTRAINT pro_con_run_id_fk
                 FOREIGN KEY (run_id)
                 REFERENCES run(run_id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE promptskim_config
                 ADD CONSTRAINT pro_con_primds_id_fk
                 FOREIGN KEY (primds_id)
                 REFERENCES primary_dataset(id)"""

        self.constraints[len(self.constraints)] = \
            """ALTER TABLE promptskim_config
                 ADD CONSTRAINT pro_con_cms_id_fk
                 FOREIGN KEY (cmssw_version_id)
                 REFERENCES cmssw_version(id)"""

        runStates = { 1 : "Active",
                      2 : "CloseOutRepack",
                      3 : "CloseOutRepackMerge",
                      4 : "CloseOutPromptReco",
                      5 : "CloseOutRecoMerge",
                      6 : "CloseOutAlcaSkim",
                      7 : "CloseOutAlcaSkimMerge",
                      8 : "CloseOutExport",
                      9 : "CloseOutT1Skimming",
                      10 : "Complete" }
        for id, name in runStates.items():
            sql = """INSERT INTO run_status
                     (ID, NAME)
                     VALUES (%d, '%s')
                     """ % (id, name)
            self.inserts[len(self.inserts)] = sql

        processingStyles = { 1 : "Bulk",
                             2 : "Express",
                             3 : "Register",
                             4 : "Convert",
                             5 : "RegisterAndConvert",
                             6 : "Ignore" }
        for id, name in processingStyles.items():
            sql = """INSERT INTO processing_style
                     (ID, NAME)
                     VALUES (%d, '%s')
                     """ % (id, name)
            self.inserts[len(self.inserts)] = sql

        eventScenarios = { 1 : "pp",
                           2 : "cosmics",
                           3 : "hcalnzs",
                           4 : "HeavyIons",
                           5 : "HeavyIonsAlcaOnly",
                           6 : "AlCaTestEnable",
                           7 : "AlCaPhiSymEcal",
                           8 : "AlCaP0" }
        for id, name in eventScenarios.items():
            sql = """INSERT INTO event_scenario
                     (ID, NAME)
                     VALUES (%d, '%s')
                     """ % (id, name)
            self.inserts[len(self.inserts)] = sql

        return

    def execute(self, conn = None, transaction = None):
        """
        _execute_

        """
        DBCreator.execute(self, conn, transaction)

        return True
