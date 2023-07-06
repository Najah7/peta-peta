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
- [`token/refresh`](#tokenrefresh)
- [`/change-passwd`](#change-passwd)
- [`/me`](#me)
- [`/users`](#users)
- [`/share-your-views`](#share-your-views)
- [`/posts`](#posts)
- [`/post-it/<post-id>`](#post-itpost-id)
- [`unpost-it/<post-it-id>`](#unpost-itpost-it-id)
- [`/like/<post-id>`](#likepost-id)
- [`/unlike/<post-id>`](#unlikepost-id)
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
  "message": "working"
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
- PUT

### パラメータ（PUT時の）
- name
- icon
- comment

### レスポンス
- 200 OK
```json
{
  "message": "success",
  "user": {
    "id": 1,
    "name": "test",
    "icon": "https://example.com/icon.png",
    "comment": "test"
  }
}
```
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
- POST

### パラメータ
- GET：ユーザの一覧取得
    - `<query>`：検索文字列（任意）
    - user-id：ユーザID（任意）

※優先度としては、user-id > query

### レスポンス
- without param
    - 200 OK
```json
[
  {
    "id": 1,
    "name": "test",
    "icon": "https://example.com/icon.png"
  },
  {
    "id": 2,
    "name": "test2",
    "icon": "https://example.com/icon2.png"
  }, ...
]
```
- 200 OK with query (value=test)
```json
[
  {
    "id": 1,
    "name": "test",
    "icon": "https://example.com/icon.png"
  },
  {
    "id": 2,
    "name": "test2",
    "icon": "https://example.com/icon2.png"
  }, ...
]
```
- 200 OK with user-id
```json
{
  "id": 1,
  "name": "test",
  "icon": "https://example.com/icon.png",
  "comment": "test"
}
```

## `/user/<user-id>`

### 概要
指定したユーザのプロフィール情報を取得する

### メソッド
- GET

### パラメータ
- user-id：ユーザID

### レスポンス
```json
{
  "name": "test",
  "icon": "https://example.com/icon.png",
  "followers": [
    {
      "id": 1,
      "name": "test",
      "icon": "https://example.com/icon.png"
    },
    {
      "id": 2,
      "name": "test2",
      "icon": "https://example.com/icon2.png"
    }, ...
  ],
  "following": [
    {
      "id": 1,
      "name": "test",
      "icon": "https://example.com/icon.png"
    },
    {
      "id": 2,
      "name": "test2",
      "icon": "https://example.com/icon2.png"
    }, ...
  ]
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
- images

### レスポンス
- 200 OK
```json
{
  "message": "success to post your views"
}
```


## `/posts`

### 概要
GET：投稿の一覧を取得する
POST with post-id：投稿の詳細を取得する
POST with query：投稿の検索を行う
※一覧と検索のときは、Likeやpost-itは件数を返す。詳細では、Likeやpost-itの一覧を返す。

### メソッド
- GET

### パラメータ
- query：検索文字列（任意）
- post-id：投稿ID（任意）

※優先度としては、post-id > query

### レスポンス
- 200 OK without params
```json
{
    {
        "title": "test",
        "content": "test",
        "user": {
            "id": 1,
            "name": "test",
            "icon": "https://example.com/icon.png"
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
        "num-post-its": 10,
        "num-likes": 10,
    }, ...
}
```
- 200 OK with query (value=test)
```json
{
    {
        "title": "test",
        "content": "test",
        "user": {
            "id": 1,
            "name": "test",
            "icon": "https://example.com/icon.png"
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
        "num-post-its": 10,
        "likes": 10,
    }, ...
}
```
- 200 OK with post-id
```json
{
    "title": "test",
    "content": "test",
    "user": {
        "id": 1,
        "name": "test",
        "icon": "https://example.com/icon.png"
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
    "post-its": [
        {
            "id": 1,
            "content": "test",
            "user": {
                "id": 1,
                "name": "test",
                "icon": "https://example.com/icon.png"
            }
        },
        {
            "id": 2,
            "content": "test2",
            "user": {
                "id": 2,
                "name": "test2",
                "icon": "https://example.com/icon2.png"
            }
        }, ...
    ],
    "likes": [
        {
            "id": 1,
            "name": "test",
            "icon": "https://example.com/icon.png"
        },
        {
            "id": 2,
            "name": "test2",
            "icon": "https://example.com/icon2.png"
        }, ...
    ],
}
```

### その他のメモ
- 一度のリクエスト何件のデータを送るか？（ページネーション）


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
    "message": "success",
    "post-it": {
        "id": 1,
        "content": "test",
        "user": {
            "id": 1,
            "name": "test",
            "icon": "https://example.com/icon.png"
        }
    }
}
```

## `/unpost-it/<post-it-id>`

### 概要
指定した付箋を削除する

### メソッド
- DELETE

### パラメータ
- post-it-id：付箋ID

### レスポンス
```json
{
    "message": "success to delete a post-it"
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
    "liked_user": {
        "id": 1,
        "name": "test",
        "icon": "https://example.com/icon.png"
    }
}
```
※👆liked_userは命名が微妙かも

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
    "unliked_user": {
        "id": 1,
        "name": "test",
        "icon": "https://example.com/icon.png"
    }
}
```
※👆liked_userは命名が微妙かも


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
    "followed_user": {
        "id": 1,
        "name": "test",
        "icon": "https://example.com/icon.png"
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
        "name": "test",
        "icon": "https://example.com/icon.png"
    }
}
```