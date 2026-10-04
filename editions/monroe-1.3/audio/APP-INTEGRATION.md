# Reader-app integration — The Fractured Path, Monroe 1.3 edition (books.worker-bee.app)

**Repo:** `/Users/drive/boundary-universe`. Its `main` auto-deploys to production through Vercel.
Work on a branch, `feature/fractured-path-monroe13`, and leave it for the coordinator to merge.

**Pattern to mirror:** the Driftwing Monroe 1.3 edition. Its IDs are `driftwing-monroe-1.3-book-0N`,
its constants live in `src/lib/catalog.ts`, its chapter paths in `src/lib/manuscript-index.ts`, and
its texts in `public/manuscripts/books/driftwing-monroe-1.3/book-0N/manuscript/`.

**Leave the current edition alone.** `book-01-the-shattered` and the rest, with their ElevenLabs
audio in the fractured-path repo, stay exactly as they are.

## Book 1 (`fractured-path-monroe-1.3-book-01`)

1. **Texts.** Copy the 60 locked chapters from
   `/Users/drive/fractured-path-monroe13/editions/monroe-1.3/book-01-the-shattered/manuscript/chapter-NN.md`
   (git tag `monroe13-book01-text-locked` plus the listening-proof fixes, i.e. the branch head) to
   `public/manuscripts/books/fractured-path-monroe-1.3/book-01/manuscript/chapter-NN.md`. Copy them
   byte for byte; the audio's `sourceSha256` depends on it.

2. **Catalog.** In `src/lib/catalog.ts`, add `FRACTURED_MONROE_BOOK_ONE_ID = "fractured-path-monroe-1.3-book-01"`
   and an entry with:
   - series "The Fractured Path";
   - title "The Shattered";
   - subtitle "The Fractured Path · Book 1 · Monroe 1.3 edition";
   - the cover the current Shattered entry uses;
   - the same `house` as the current Shattered entry;
   - `totalChapters` 60;
   - a two-sentence synopsis and a description in the house register. No spoilers past chapter 5.
   - a `seriesIndex` that places it beside the current Book 1 without displacing it.

3. **Manuscript index.** In `src/lib/manuscript-index.ts`, add 60 entries. Each needs a number, the
   title from the chapter's H1 with the "Chapter N — " prefix stripped (follow the existing
   convention), and the path.

4. **Audio.** The renders are published by `editions/monroe-1.3/audio/fp_publish.py` to the
   fractured-path repo's `main`, at `audio/fractured-path-monroe-1.3-book-01/chapter-NN.mp3` (LFS),
   with a book entry in `audio/manifest.json`. The app already reads `FRACTURED_MANIFEST_URL` and
   `peekFracturedAudio`.
   - Raise the `numbers` validator in `src/lib/fractured-audio.ts` from max 40 to 80, in both the
     element and the array.
   - Confirm that the new book's chapters resolve through `${base}/${bookId}/chapter-NN.mp3`.
   - Confirm that the manifest merge (`pickRicherManifest`) surfaces the new book.
   - Check that the player shows the render's `voice` and `note`, the "listening audition"
     licence label (owner decision #34).

5. **Verify.**
   - Run `npm run build` and `node --test` on the existing tests (e.g. `scripts/*.test.mjs`).
   - Run the dev server, open the new book, and confirm that chapters 1 and 60 render as text.
   - Confirm that chapter 1's audio plays once `fp_publish.py` has published it.
   - Take a mobile screenshot of the book page.
   - Push the branch. Do not merge to `main`; report back instead.

## Later books

Add the same entries as each book's text locks: `fractured-path-monroe-1.3-book-0N`. Extend the
`BOOKS` map in `fp_publish.py` at the same time.
