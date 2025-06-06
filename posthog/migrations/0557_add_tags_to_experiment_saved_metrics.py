# Generated by Django 4.2.18 on 2025-01-30 17:45

from django.db import migrations, models
import django.db.models.deletion

# Original migration is a single transaction, but CREATE INDEX CONCURRENTLY can't run in a transaction.
# As such, we need to run a bunch of separate statements.
#
# BEGIN;
# --
# -- Remove constraint exactly_one_related_object from model taggeditem
# --
# ALTER TABLE "posthog_taggeditem" DROP CONSTRAINT "exactly_one_related_object";
# --
# -- Alter unique_together for taggeditem (0 constraint(s))
# --
# ALTER TABLE "posthog_taggeditem" DROP CONSTRAINT "posthog_taggeditem_tag_id_dashboard_id_insi_a13e3a20_uniq";
# --
# -- Add field experiment_saved_metric to taggeditem
# --
# ALTER TABLE "posthog_taggeditem" ADD COLUMN "experiment_saved_metric_id" integer NULL CONSTRAINT "posthog_taggeditem_experiment_saved_met_b6af2199_fk_posthog_e" REFERENCES "posthog_experimentsavedmetric"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "posthog_taggeditem_experiment_saved_met_b6af2199_fk_posthog_e" IMMEDIATE;
# --
# -- Alter unique_together for taggeditem (1 constraint(s))
# --
# ALTER TABLE "posthog_taggeditem" ADD CONSTRAINT "posthog_taggeditem_tag_id_dashboard_id_insi_734394e1_uniq" UNIQUE ("tag_id", "dashboard_id", "insight_id", "event_definition_id", "property_definition_id", "action_id", "feature_flag_id", "experiment_saved_metric_id");
# --
# -- Create constraint unique_experiment_saved_metric_tagged_item on model taggeditem
# --
# CREATE UNIQUE INDEX "unique_experiment_saved_metric_tagged_item" ON "posthog_taggeditem" ("tag_id", "experiment_saved_metric_id") WHERE "experiment_saved_metric_id" IS NOT NULL;
# --
# -- Create constraint exactly_one_related_object on model taggeditem
# --
# ALTER TABLE "posthog_taggeditem"
# ADD CONSTRAINT "exactly_one_related_object"
# CHECK ((
#     ("dashboard_id" IS NOT NULL AND "insight_id" IS NULL AND "event_definition_id" IS NULL AND "property_definition_id" IS NULL AND "action_id" IS NULL AND "feature_flag_id" IS NULL AND "experiment_saved_metric_id" IS NULL) OR
#     ("dashboard_id" IS NULL AND "insight_id" IS NOT NULL AND "event_definition_id" IS NULL AND "property_definition_id" IS NULL AND "action_id" IS NULL AND "feature_flag_id" IS NULL AND "experiment_saved_metric_id" IS NULL) OR
#     ("dashboard_id" IS NULL AND "insight_id" IS NULL AND "event_definition_id" IS NOT NULL AND "property_definition_id" IS NULL AND "action_id" IS NULL AND "feature_flag_id" IS NULL AND "experiment_saved_metric_id" IS NULL) OR
#     ("dashboard_id" IS NULL AND "insight_id" IS NULL AND "event_definition_id" IS NULL AND "property_definition_id" IS NOT NULL AND "action_id" IS NULL AND "feature_flag_id" IS NULL AND "experiment_saved_metric_id" IS NULL) OR
#     ("dashboard_id" IS NULL AND "insight_id" IS NULL AND "event_definition_id" IS NULL AND "property_definition_id" IS NULL AND "action_id" IS NOT NULL AND "feature_flag_id" IS NULL AND "experiment_saved_metric_id" IS NULL) OR
#     ("dashboard_id" IS NULL AND "insight_id" IS NULL AND "event_definition_id" IS NULL AND "property_definition_id" IS NULL AND "action_id" IS NULL AND "feature_flag_id" IS NOT NULL AND "experiment_saved_metric_id" IS NULL) OR
#     ("dashboard_id" IS NULL AND "insight_id" IS NULL AND "event_definition_id" IS NULL AND "property_definition_id" IS NULL AND "action_id" IS NULL AND "feature_flag_id" IS NULL AND "experiment_saved_metric_id" IS NOT NULL)
# ));
# CREATE INDEX "posthog_taggeditem_experiment_saved_metric_id_b6af2199" ON "posthog_taggeditem" ("experiment_saved_metric_id");
# COMMIT;


class Migration(migrations.Migration):
    atomic = False  # Added to support concurrent index creation
    dependencies = [
        ("posthog", "0556_add_execution_order_to_hog_functions"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveConstraint(
                    model_name="taggeditem",
                    name="exactly_one_related_object",
                ),
                migrations.AlterUniqueTogether(
                    name="taggeditem",
                    unique_together=set(),
                ),
                migrations.AddField(
                    model_name="taggeditem",
                    name="experiment_saved_metric",
                    field=models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagged_items",
                        to="posthog.experimentsavedmetric",
                    ),
                ),
                migrations.AlterUniqueTogether(
                    name="taggeditem",
                    unique_together={
                        (
                            "tag",
                            "dashboard",
                            "insight",
                            "event_definition",
                            "property_definition",
                            "action",
                            "feature_flag",
                            "experiment_saved_metric",
                        )
                    },
                ),
                migrations.AddConstraint(
                    model_name="taggeditem",
                    constraint=models.UniqueConstraint(
                        condition=models.Q(("experiment_saved_metric__isnull", False)),
                        fields=("tag", "experiment_saved_metric"),
                        name="unique_experiment_saved_metric_tagged_item",
                    ),
                ),
                migrations.AddConstraint(
                    model_name="taggeditem",
                    constraint=models.CheckConstraint(
                        check=models.Q(
                            models.Q(
                                ("dashboard__isnull", False),
                                ("insight__isnull", True),
                                ("event_definition__isnull", True),
                                ("property_definition__isnull", True),
                                ("action__isnull", True),
                                ("feature_flag__isnull", True),
                                ("experiment_saved_metric__isnull", True),
                            ),
                            models.Q(
                                ("dashboard__isnull", True),
                                ("insight__isnull", False),
                                ("event_definition__isnull", True),
                                ("property_definition__isnull", True),
                                ("action__isnull", True),
                                ("feature_flag__isnull", True),
                                ("experiment_saved_metric__isnull", True),
                            ),
                            models.Q(
                                ("dashboard__isnull", True),
                                ("insight__isnull", True),
                                ("event_definition__isnull", False),
                                ("property_definition__isnull", True),
                                ("action__isnull", True),
                                ("feature_flag__isnull", True),
                                ("experiment_saved_metric__isnull", True),
                            ),
                            models.Q(
                                ("dashboard__isnull", True),
                                ("insight__isnull", True),
                                ("event_definition__isnull", True),
                                ("property_definition__isnull", False),
                                ("action__isnull", True),
                                ("feature_flag__isnull", True),
                                ("experiment_saved_metric__isnull", True),
                            ),
                            models.Q(
                                ("dashboard__isnull", True),
                                ("insight__isnull", True),
                                ("event_definition__isnull", True),
                                ("property_definition__isnull", True),
                                ("action__isnull", False),
                                ("feature_flag__isnull", True),
                                ("experiment_saved_metric__isnull", True),
                            ),
                            models.Q(
                                ("dashboard__isnull", True),
                                ("insight__isnull", True),
                                ("event_definition__isnull", True),
                                ("property_definition__isnull", True),
                                ("action__isnull", True),
                                ("feature_flag__isnull", False),
                                ("experiment_saved_metric__isnull", True),
                            ),
                            models.Q(
                                ("dashboard__isnull", True),
                                ("insight__isnull", True),
                                ("event_definition__isnull", True),
                                ("property_definition__isnull", True),
                                ("action__isnull", True),
                                ("feature_flag__isnull", True),
                                ("experiment_saved_metric__isnull", False),
                            ),
                            _connector="OR",
                        ),
                        name="exactly_one_related_object",
                    ),
                ),
            ],
            database_operations=[
                migrations.RunSQL(
                    """
                    ALTER TABLE "posthog_taggeditem" ADD COLUMN "experiment_saved_metric_id" integer NULL CONSTRAINT "posthog_taggeditem_experiment_saved_met_b6af2199_fk_posthog_e" REFERENCES "posthog_experimentsavedmetric"("id") DEFERRABLE INITIALLY DEFERRED; -- existing-table-constraint-ignore
                    SET CONSTRAINTS "posthog_taggeditem_experiment_saved_met_b6af2199_fk_posthog_e" IMMEDIATE; -- existing-table-constraint-ignore
                    """,
                    reverse_sql="""
                        ALTER TABLE "posthog_taggeditem" DROP COLUMN IF EXISTS "experiment_saved_metric_id";
                    """,
                ),
                migrations.RunSQL(
                    """
                    CREATE INDEX CONCURRENTLY "posthog_taggeditem_experiment_saved_metric_id_b6af2199" ON "posthog_taggeditem" ("experiment_saved_metric_id");
                    """,
                    reverse_sql="""
                        DROP INDEX IF EXISTS "posthog_taggeditem_experiment_saved_metric_id_b6af2199";
                    """,
                ),
                migrations.RunSQL(
                    """
                    CREATE UNIQUE INDEX CONCURRENTLY "unique_experiment_saved_metric_tagged_item" ON "posthog_taggeditem" ("tag_id", "experiment_saved_metric_id") WHERE "experiment_saved_metric_id" IS NOT NULL; -- not-null-ignore
                    """,
                    reverse_sql="""
                        DROP INDEX IF EXISTS "unique_experiment_saved_metric_tagged_item";
                    """,
                ),
                migrations.RunSQL(
                    """
                    ALTER TABLE "posthog_taggeditem" DROP CONSTRAINT "exactly_one_related_object";
                    ALTER TABLE "posthog_taggeditem" ADD CONSTRAINT "exactly_one_related_object" CHECK ( /* -- existing-table-constraint-ignore */
                            (
                                (dashboard_id IS NOT NULL AND insight_id IS NULL AND event_definition_id IS NULL AND property_definition_id IS NULL AND action_id IS NULL AND feature_flag_id IS NULL AND experiment_saved_metric_id IS NULL) OR /* -- not-null-ignore */
                                (dashboard_id IS NULL AND insight_id IS NOT NULL AND event_definition_id IS NULL AND property_definition_id IS NULL AND action_id IS NULL AND feature_flag_id IS NULL AND experiment_saved_metric_id IS NULL) OR /* -- not-null-ignore */
                                (dashboard_id IS NULL AND insight_id IS NULL AND event_definition_id IS NOT NULL AND property_definition_id IS NULL AND action_id IS NULL AND feature_flag_id IS NULL AND experiment_saved_metric_id IS NULL) OR /* -- not-null-ignore */
                                (dashboard_id IS NULL AND insight_id IS NULL AND event_definition_id IS NULL AND property_definition_id IS NOT NULL AND action_id IS NULL AND feature_flag_id IS NULL AND experiment_saved_metric_id IS NULL) OR /* -- not-null-ignore */
                                (dashboard_id IS NULL AND insight_id IS NULL AND event_definition_id IS NULL AND property_definition_id IS NULL AND action_id IS NOT NULL AND feature_flag_id IS NULL AND experiment_saved_metric_id IS NULL) OR /* -- not-null-ignore */
                                (dashboard_id IS NULL AND insight_id IS NULL AND event_definition_id IS NULL AND property_definition_id IS NULL AND action_id IS NULL AND feature_flag_id IS NOT NULL AND experiment_saved_metric_id IS NULL) OR /* -- not-null-ignore */
                                (dashboard_id IS NULL AND insight_id IS NULL AND event_definition_id IS NULL AND property_definition_id IS NULL AND action_id IS NULL AND feature_flag_id IS NULL AND experiment_saved_metric_id IS NOT NULL) /* -- not-null-ignore */
                            )
                        ) NOT VALID;
                    """,
                    reverse_sql="""
                        ALTER TABLE "posthog_taggeditem" DROP CONSTRAINT "exactly_one_related_object";
                        ALTER TABLE "posthog_taggeditem" ADD CONSTRAINT "exactly_one_related_object" CHECK ( /* -- existing-table-constraint-ignore */
                            (
                                (dashboard_id IS NOT NULL AND insight_id IS NULL AND event_definition_id IS NULL AND property_definition_id IS NULL AND action_id IS NULL AND feature_flag_id IS NULL) OR /* -- not-null-ignore */
                                (dashboard_id IS NULL AND insight_id IS NOT NULL AND event_definition_id IS NULL AND property_definition_id IS NULL AND action_id IS NULL AND feature_flag_id IS NULL) OR /* -- not-null-ignore */
                                (dashboard_id IS NULL AND insight_id IS NULL AND event_definition_id IS NOT NULL AND property_definition_id IS NULL AND action_id IS NULL AND feature_flag_id IS NULL) OR /* -- not-null-ignore */
                                (dashboard_id IS NULL AND insight_id IS NULL AND event_definition_id IS NULL AND property_definition_id IS NOT NULL AND action_id IS NULL AND feature_flag_id IS NULL) OR /* -- not-null-ignore */
                                (dashboard_id IS NULL AND insight_id IS NULL AND event_definition_id IS NULL AND property_definition_id IS NULL AND action_id IS NOT NULL AND feature_flag_id IS NULL) OR /* -- not-null-ignore */
                                (dashboard_id IS NULL AND insight_id IS NULL AND event_definition_id IS NULL AND property_definition_id IS NULL AND action_id IS NULL AND feature_flag_id IS NOT NULL) /* -- not-null-ignore */
                            )
                        ) NOT VALID;
                    """,
                ),
                migrations.RunSQL(
                    """
                    ALTER TABLE "posthog_taggeditem" DROP CONSTRAINT IF EXISTS "posthog_taggeditem_tag_id_dashboard_id_insi_a13e3a20_uniq";
                    """,
                    # Intentially swapped with below because these three statements go together.
                    reverse_sql="""
                        ALTER TABLE "posthog_taggeditem" ADD CONSTRAINT "posthog_taggeditem_tag_id_dashboard_id_insi_a13e3a20_uniq" UNIQUE USING INDEX "posthog_taggeditem_tag_id_dashboard_id_insi_a13e3a20_uniq"; -- existing-table-constraint-ignore
                    """,
                ),
                # This statement doesn't need to be reversed because it's always the middle of the three statements.
                migrations.RunSQL(
                    """
                    CREATE UNIQUE INDEX CONCURRENTLY IF NOT EXISTS "posthog_taggeditem_tag_id_dashboard_id_insi_734394e1_uniq" ON "posthog_taggeditem" ("tag_id", "dashboard_id", "insight_id", "event_definition_id", "property_definition_id", "action_id", "feature_flag_id", "experiment_saved_metric_id");
                    """,
                    reverse_sql="""
                        CREATE UNIQUE INDEX CONCURRENTLY IF NOT EXISTS "posthog_taggeditem_tag_id_dashboard_id_insi_a13e3a20_uniq" ON "posthog_taggeditem" ("tag_id", "dashboard_id", "insight_id", "event_definition_id", "property_definition_id", "action_id", "feature_flag_id");
                    """,
                ),
                migrations.RunSQL(
                    """
                    ALTER TABLE "posthog_taggeditem" ADD CONSTRAINT "posthog_taggeditem_tag_id_dashboard_id_insi_734394e1_uniq" UNIQUE USING INDEX "posthog_taggeditem_tag_id_dashboard_id_insi_734394e1_uniq"; -- existing-table-constraint-ignore
                    """,
                    # Intentially swapped with above because these three statements go together.
                    reverse_sql="""
                        ALTER TABLE "posthog_taggeditem" DROP CONSTRAINT IF EXISTS "posthog_taggeditem_tag_id_dashboard_id_insi_734394e1_uniq";
                    """,
                ),
            ],
        )
    ]
