CREATE TABLE IF NOT EXISTS recommendations (
  post_key TEXT PRIMARY KEY,
  count INTEGER NOT NULL DEFAULT 0,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS recommendation_votes (
  post_key TEXT NOT NULL,
  voter_hash TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (post_key, voter_hash)
);

CREATE INDEX IF NOT EXISTS idx_recommendation_votes_post_key
  ON recommendation_votes (post_key);
