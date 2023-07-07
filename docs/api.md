# API設計

## 前提
下記は、画像の投稿機能用のエンドポントの設計<br>
設計で示した内容は下記<br>
- エンドポントの概要
- パラメータ
- 正常時のレスポンス<br>
※正常時のレスポンスのみ記述（エラー時のレスポンスのは、フレームワークなどのデフォルトのレスポンスを使うつもりなので、あえて設計では省略）

## 機能一覧
- トークン認証(トークン取得、更新)（email & password）
- メールでのパスワードの変更
- プロフィールの閲覧 & 更新
- ユーザの表示 & 検索
- 投稿
- 投稿の表示 & 検索
- コメント(post-it)の追加 & 削除
- 投稿にいいねの追加 & 削除
- フォローの追加 & 削除




## エンドポイント一覧
- [`/healthcheck`](#healthcheck)
- [`/token`](#token)
- [`/token/refresh`](#tokenrefresh)
- [`/change-passwd`](#change-passwd)
- [`/me`](#me)
- [`/users`](#users)
- [`/share-your-views`](#share-your-views)
- [`/upload-image`](#upload-image)
- [`/posts`](#posts)
- [`/post-it/<post-id>`](#post-itpost-id)
- [`/unpost-it/<sticky-note-id>`](#unpost-itsticky-note-id)
- [`/like/<post-id>`](#likepost-id)
- [`/unlike/<post-id>`](#unlikepost-id)
- [`/like/<sticky-note-id>`](#likesticky-note-id)
- [`/unlike/<sticky-note-id>`](#unlikesticky-note-id)
- [`/follow/<user-id>`](#followuser-id)
- [`/unfollow/<user-id>`](#unfollowuser-id)

## エンドポイント詳細

### `/healthcheck`

#### 概要
ヘルスチェック用

#### メソッド
- GET

#### パラメータ
なし

#### レスポンス
- 200 OK
```json
{
  "message": "Server is working"
}
```


## `/token`

### 概要
認証用のトークンを取得する

### メソッド
- POST

### パラメータ
- email
- password

### レスポンス
- 200 OK
```json
{
  "token": "xxx"
}
```

## `/token/refresh`

### 概要
トークンを更新する

### メソッド
- POST

### パラメータ
- token

### レスポンス
```json
{
  "token": "xxx"
}
```


## `/me`

### 概要
プロフィールの閲覧・更新を行う。<br>
トークンの情報により、ユーザを特定する。

### メソッド
- GET
- PATCH

### パラメータ（PATCH時の）
- name
- icon
- comment

### レスポンス
- 200 OK
```json
{
  "id": 1,
  "name": "test太郎",
  "icon-url": "https://example.com/icon.png",
  "comment": "describe yourself",
  "posts": [
    {
      "id": 1,
      "title": "test title",
      "content": "test content",
      "images": "https://example.com/image.png",
      "created_at": "2020-01-01 00:00:00",
      "updated_at": "2020-01-01 00:00:00"
    },
    {
      "id": 2,
      "title": "test2 title",
      "content": "test2 content",
      "images": "https://example.com/image2.png",
      "created_at": "2020-01-01 00:00:00",
      "updated_at": "2020-01-01 00:00:00"
    }, ...
    ],
}
```
※ユーザページでは最初の写真のみ表示すると仮定

※tokenからユーザを特定

- 200 OK when PATCH
```json
{
  "message": "success to update",
  "user": {
    "id": 1,
    "name": "new test太郎",
    "icon-url": "https://example.com/icon.png",
    "comment": "new description",
    "posts": [
      {
        "id": 1,
        "title": "test title",
        "content": "test content",
        "images": "https://example.com/image.png",
        "created_at": "2020-01-01 00:00:00",
        "updated_at": "2020-01-01 00:00:00"
      },
      {
        "id": 2,
        "title": "test2 title",
        "content": "test2 content",
        "images": "https://example.com/image2.png",
        "created_at": "2020-01-01 00:00:00",
        "updated_at": "2020-01-01 00:00:00"
      }, ...
      ],
  }
}
```

※ユースケース的にGETする前にPATCHすることはないかも。だとしたら、postsはPATCH時には返さない方がいいかも

### その他ノート
どんな要素を持たせるかは考え中

## `/change-passwd`

### 概要
メールを使って、パスワードを変更する

### メソッド
- POST

### パラメータ
- email

### レスポンス
- 200 OK
```json
{
  "message": "success to send email"
}
```

## `/users`

### 概要
ユーザ一覧を取得する

### メソッド
- GET

### パラメータ
- query：検索文字列（任意）

※優先度としては、user-id > query

### レスポンス
- without param
    - 200 OK
```json
[
  {
    "id": 1,
    "name": "test太郎",
    "icon-url": "https://example.com/icon.png",
    "comment": "describe yourself",
  },
  {
    "id": 2,
    "name": "test2太郎",
    "icon-url": "https://example.com/icon2.png",
    "comment": "describe yourself",
  }, ...
]
```
- 200 OK with query (value=test)
```json
[
  {
    "id": 1,
    "name": "test太郎",
    "icon-url": "https://example.com/icon.png",
    "comment": "describe yourself",
  },
  {
    "id": 2,
    "name": "test2太郎",
    "icon-url": "https://example.com/icon2.png",
    "comment": "describe yourself",
  }, ...
]
```
## `/user/<user-id>`

### 概要
指定したユーザのプロフィール情報の詳細を取得する

### メソッド
- GET

### パラメータ
- user-id：ユーザID

### レスポンス
```json
{
  "name": "test太郎",
  "icon-url": "https://example.com/icon.png",
  "comment": "describe yourself",
  "followers": [
    {
      "id": 1,
      "name": "test太郎",
      "icon-url": "https://example.com/icon.png"
    },
    {
      "id": 2,
      "name": "test2太郎",
      "icon-url": "https://example.com/icon2.png"
    }, ...
  ],
  "following": [
    {
      "id": 1,
      "name": "test太郎",
      "icon-url": "https://example.com/icon.png"
    },
    {
      "id": 2,
      "name": "test2太郎",
      "icon-url": "https://example.com/icon2.png"
    }, ...
  ],
  "post": {
    "id": 1,
    "title": "test title",
    "content": "test content",
    "images": [
      {
        "id": 1,
        "url": "https://example.com/image.png"
      },
      {
        "id": 2,
        "url": "https://example.com/image2.png"
      }, ...
    ]
  }
}
```

## `/share-your-views`

### 概要
投稿を行う

### メソッド
- POST

### パラメータ
- title
- content
- seat
- images-urls


※ images-urlsはupload-imageで取得した画像オブジェクトの配列

### レスポンス
- 200 OK
```json
{
  "message": "success to share your views",
  "post" :{
    "title": "test title",
    "content": "test content",
    "seat": "A-1",
    "images" : [
      {
        "id": 1,
        "url": "https://example.com/image.png"
      },
      {
        "id": 2,
        "url": "https://example.com/image2.png"
      }, ...
    ]
  }
}
```

## `/upload-image`

### 概要
画像をアップロードする

### メソッド
- POST

### パラメータ
- image

### レスポンス
- 200 OK
```json
{
  "message": "success to upload image",
  "image": {
    "id": 1,
    "url": "https://example.com/image.png"
  }
}
```

## `/posts`

### 概要
GET：投稿の一覧を取得する
POST with query：投稿の検索を行う（とりあえずタイトル検索のつもり）
※一覧と検索のときは、Likeは件数を返す。

### メソッド
- GET

### パラメータ
- query：検索文字列（任意）


※優先度としては、post-id > query

### レスポンス
- 200 OK without params
```json
[
  {
      "title": "test title",
      "content": "test content",
      "seat": "A-1",
      "num-likes": 10,
      "user": {
          "id": 1,
          "name": "test太郎",
          "icon-url": "https://example.com/icon.png"
      },
      "images": [
          {
              "id": 1,
              "url": "https://example.com/image.png"
          },
          {
              "id": 2,
              "url": "https://example.com/image2.png"
          }, ...
      ],
      "sticky-notes": {
          "id": 1,
          "content": "test content",
          "color": "red",
          "num-likes": 10,
          "user": {
              "id": 1,
              "name": "test太郎",
              "icon-url": "https://example.com/icon.png"
          },
      }
  },
  {
      "title": "test title",
      "content": "test content",
      "seat": "A-1",
      "num-likes": 10,
      "user": {
          "id": 1,
          "name": "test太郎",
          "icon-url": "https://example.com/icon.png"
      },
      "images": [
          {
              "id": 1,
              "url": "https://example.com/image.png"
          },
          {
              "id": 2,
              "url": "https://example.com/image2.png"
          }, ...
      ],
      "sticky-notes": [
            {
              "id": 1,
              "content": "test content",
              "color": "red",
              "num-likes": 10,
              "user": {
                "id": 1,
                "name": "test太郎",
                "icon-url": "https://example.com/icon.png"
              }
          },
          {
              "id": 2,
              "content": "test content",
              "color": "red",
              "num-likes": 10,
              "user": {
                  "id": 1,
                  "name": "test太郎",
                  "icon-url": "https://example.com/icon.png"
              },
          }, ...
      ]
  }, ...
]
```

※sticky-noteはいいねが多い順でソートして数個返すのもあり

- 200 OK with query (value=test)
```json
[
  {
      "title": "test in title",
      "content": "test content",
      "seat": "A-1",
      "num-likes": 10,
      "user": {
          "id": 1,
          "name": "test太郎",
          "icon-url": "https://example.com/icon.png"
      },
      "images": [
          {
              "id": 1,
              "url": "https://example.com/image.png"
          },
          {
              "id": 2,
              "url": "https://example.com/image2.png"
          }, ...
      ],
      "sticky-notes": [
            {
              "id": 1,
              "content": "test content",
              "color": "red",
              "num-likes": 10,
              "user": {
                "id": 1,
                "name": "test太郎",
                "icon-url": "https://example.com/icon.png"
              }
          },
          {
              "id": 2,
              "content": "test content",
              "color": "red",
              "num-likes": 10,
              "user": {
                  "id": 1,
                  "name": "test太郎",
                  "icon-url": "https://example.com/icon.png"
              },
          }, ...
      ]
  },
  {
      "title": "test in title",
      "content": "test content",
      "seat": "A-1",
      "num-likes": 10,
      "user": {
          "id": 1,
          "name": "test太郎",
          "icon-url": "https://example.com/icon.png"
      },
      "images": [
          {
              "id": 1,
              "url": "https://example.com/image.png"
          },
          {
              "id": 2,
              "url": "https://example.com/image2.png"
          }, ...
      ],
      "sticky-notes": [
          "id": 1,
          "content": "test content",
          "color": "red",
          "num-likes": 10,
          "user": {
              "id": 1,
              "name": "test太郎",
              "icon-url": "https://example.com/icon.png"
          },
      ]
  }, ...
]
```

※sticky-noteはいいねが多い順でソートして数個返すのもあり
### その他のメモ
- 一度のリクエスト何件のデータを送るか？（ページネーション）

## `/post/<post-id>`

### 概要
指定した投稿の詳細を取得する

### メソッド
- GET

### パラメータ
- post-id：投稿ID

### レスポンス
```json
{
    "title": "test title",
    "content": "test content",
    "seat": "A-1",
    "num-likes": 10,
    "user": {
        "id": 1,
        "name": "test太郎",
        "icon-url": "https://example.com/icon.png"
    },
    "images": [
        {
            "id": 1,
            "url": "https://example.com/image.png"
        },
        {
            "id": 2,
            "url": "https://example.com/image2.png"
        }, ...
    ],
    "sticky-notes": [
        "id": 1,
        "content": "test content",
        "color": "red",
        "num-likes": 10,
        "user": {
            "id": 1,
            "name": "test太郎",
            "icon-url": "https://example.com/icon.png"
        },
    ]
}
```

※sticky-noteはいいねが多い順でソートして数個返すのもあり


## `/post-it/<post-id>`

### 概要
指定した投稿に付箋をつける

### メソッド
- POST

### パラメータ
- post-id：投稿ID
- content：付箋の内容
- color：付箋の色

### レスポンス
```json
{
    "message": "success to create a sticky note",
    "sticky-note": {
        "id": 1,
        "content": "test content",
        "color": "red",
        "user": {
            "id": 1,
            "name": "test太郎",
            "icon-url": "https://example.com/icon.png"
        }
    }
}
```

## `/unpost-it/<sticky-note-id>`

### 概要
指定した付箋を削除する

### メソッド
- DELETE

### パラメータ
- sticky-note-id：付箋ID

### レスポンス
```json
{
    "message": "success to delete a sticky note",
    "sticky-note": {
        "id": 1,
        "content": "test content",
        "color": "red",
        "user": {
            "id": 1,
            "name": "test太郎",
            "icon-url": "https://example.com/icon.png"
        }
    }
}
```


## `/like/<post-id>`

### 概要
指定した投稿にいいねをつける

### メソッド
- POST

### パラメータ
- post-id：投稿ID

### レスポンス
```json
{
    "message": "success to like a post",
    "liked_post": {
        "id": 1,
        "title": "test title",
        "content": "test content",
        "seat": "A-1",
        "user": {
            "id": 1,
            "name": "test太郎",
            "icon-url": "https://example.com/icon.png"
        },
        "images": [
            {
                "id": 1,
                "url": "https://example.com/image.png"
            },
            {
                "id": 2,
                "url": "https://example.com/image2.png"
            }, ...
        ],
        "num-sticky-notes": 10,
        "num-likes": 10,
    },
}
```
※👆liked_postは命名が微妙かも

## `/unlike/<post-id>`

### 概要
指定した投稿のいいねを解除する

### メソッド
- DELETE

### パラメータ
- post-id：投稿ID

### レスポンス
```json
{
    "message": "success to unlike a post",
    "unliked-post": {
        "id": 1,
        "title": "test title",
        "content": "test content",
        "seat": "A-1",
        "user": {
            "id": 1,
            "name": "test太郎",
            "icon-url": "https://example.com/icon.png"
        },
        "images": [
            {
                "id": 1,
                "url": "https://example.com/image.png"
            },
            {
                "id": 2,
                "url": "https://example.com/image2.png"
            }, ...
        ],
        "num-sticky-notes": 10,
        "num-likes": 10,
    },
    }
}
```
※👆unliked-postは命名が微妙かも

## `/like/<sticky-note-id>`

### 概要
指定した付箋にいいねをつける

### メソッド
- POST

### パラメータ
- sticky-note-id：付箋ID

### レスポンス
```json
{
    "message": "success to like a sticky note",
    "liked-sticky-note": {
        "id": 1,
        "content": "test content",
        "color": "red",
        "user": {
            "id": 1,
            "name": "test太郎",
            "icon-url": "https://example.com/icon.png"
        }
    }
}
```

## `/unlike/<sticky-note-id>`

### 概要
指定した付箋のいいねを解除する

### メソッド
- DELETE

### パラメータ
- sticky-note-id：付箋ID

### レスポンス
```json
{
    "message": "success to unlike a sticky note",
    "unliked-sticky-note": {
        "id": 1,
        "content": "test content",
        "color": "red",
        "user": {
            "id": 1,
            "name": "test太郎",
            "icon-url": "https://example.com/icon.png"
        }
    }
}
```


## `/follow/<user-id>`

### 概要
指定したユーザをフォローする

### メソッド
- POST

### パラメータ
- user-id：ユーザID

### レスポンス
```json
{
    "message": "success to follow a user",
    "followed-user": {
        "id": 1,
        "name": "test太郎",
        "icon-url": "https://example.com/icon.png"
    }
}
```

## `/unfollow/<user-id>`

### 概要
指定したユーザのフォローを解除する

### メソッド
- DELETE

### パラメータ
- user-id：ユーザID

### レスポンス
```json
{
    "message": "success to unfollow a user",
    "unfollowed_user": {
        "id": 1,
        "name": "test太郎",
        "icon-url": "https://example.com/icon.png"
    }
}
```